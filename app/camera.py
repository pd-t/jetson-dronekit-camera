import os
import re
import threading
import logging
import jetson.utils


class CameraManager:
    def __init__(self,
                 video_source: str,
                 output_directory: str):
        self.camera = Camera(video_source=video_source)
        self.video_output = self.__create_video_output(video_source,
                                                       output_directory)
        self.logger = self.__create_logger(video_source,
                                           output_directory)
        self.image = None

    @staticmethod
    def __get_source_name(video_source):
        source_name = re.sub('[^A-Za-z0-9]+', '', video_source)
        return source_name

    def __create_video_output(self, video_source: str, output_directory: str):
        source_name = self.__get_source_name(video_source)
        video_output = 'file://' + os.path.join(output_directory,
                                                source_name + '_%i.jpg')
        return jetson.utils.videoOutput(video_output)

    def __create_logger(self, video_source: str, output_directory: str):
        source_name = self.__get_source_name(video_source)
        logger = logging.getLogger(source_name)
        logger.setLevel(logging.INFO)
        log_filename = os.path.join(output_directory,
                                    source_name + '.log')
        fh = logging.FileHandler(log_filename)
        fh.setLevel(logging.INFO)
        logger.addHandler(fh)
        formatter = logging.Formatter('%(asctime)s;'
                                      '%(name)s;'
                                      '%(levelname)s;'
                                      '%(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

    def startup(self):
        self.logger.info('camera startup')
        self.camera.start()

    def capture(self):
        self.logger.info('image capture')
        self.image = self.camera.read()

    def save(self):
        self.video_output.Render(self.image)

    def shutdown(self):
        self.logger.info('camera shutdown')
        self.camera.stop()
        self.camera.release()


class Camera:
    def __init__(self, video_source: str):
        self.video_capture = jetson.utils.videoSource(video_source)
        self.frame = None
        self.read_thread = None
        self.read_lock = threading.Lock()
        self.running = False

    def start(self):
        if self.running:
            print('Video capturing is already running')
            return None
        if self.video_capture is not None:
            self.running = True
            self.read_thread = threading.Thread(target=self.update_camera)
            self.read_thread.start()

    def stop(self):
        self.running = False
        self.read_thread.join()

    def update_camera(self):
        while self.running:
            self.frame = self.video_capture.Capture()

    def read(self):
        return self.frame

    def release(self):
        if self.read_thread is not None:
            self.read_thread.join()
