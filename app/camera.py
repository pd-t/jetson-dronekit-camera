import threading
import jetson.utils


class CameraManager:
    def __init__(self,
                 video_source: str,
                 video_output: str):
        self.camera = Camera(video_source=video_source)
        self.video_output = jetson.utils.videoOutput(video_output)
        self.image = None

    def startup(self):
        self.camera.start()

    def capture(self):
        self.image = self.camera.read()

    def save(self):
        self.video_output.Render(self.image)

    def shutdown(self):
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
