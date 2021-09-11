import jetson.utils
from time import sleep
import threading

left_camera = None
right_camera = None


class CSICamera:

    def __init__(self):
        self.video_capture = None
        self.frame = None
        self.read_thread = None
        self.read_lock = threading.Lock()
        self.running = False

    def open(self, sensor_id):
        self.video_capture = jetson.utils.videoSource('csi://' + str(sensor_id))

    def start(self):
        if self.running:
            print('Video capturing is already running')
            return None
        if self.video_capture != None:
            self.running = True
            self.read_thread = threading.Thread(target=self.update_camera)
            self.read_thread.start()
        return self

    def stop(self):
        self.running = False
        self.read_thread.join()

    def update_camera(self):
        while self.running:
            self.frame = self.video_capture.Capture()

    def read(self):
        return self.frame

    def release(self):
        if self.read_thread != None:
            self.read_thread.join()


def start_cameras():
    left_camera = CSICamera()
    left_camera.open(sensor_id=0)
    left_camera.start()

    right_camera = CSICamera()
    right_camera.open(sensor_id=1)
    right_camera.start()

    output_cam_0 = jetson.utils.videoOutput('file:///data/image_%i_cam0.jpg')
    output_cam_1 = jetson.utils.videoOutput('file:///data/image_%i_cam1.jpg')

    for i in range(5):
        print(i)
        left_image = left_camera.read()
        right_image = right_camera.read()
        output_cam_0.Render(left_image)
        output_cam_1.Render(right_image)
        sleep(5)

    left_camera.stop()
    left_camera.release()
    right_camera.stop()
    right_camera.release()


if __name__ == "__main__":
    start_cameras()
