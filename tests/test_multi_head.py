from app.camera import CameraManager
from app.multiheadcamera import MultiHeadCamera
from time import sleep


def test_multi_head():
    multi_head_camera = MultiHeadCamera(video_sources=['csi://0', 'csi://1'],
                                        output_directory='/data/test')
    for i in range(3):
        multi_head_camera.capture()
        sleep(1)
    del multi_head_camera
