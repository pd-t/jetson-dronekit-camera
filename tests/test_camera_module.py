from app.camera_manager import CameraManager
from app.jetson_camera import JetsonCamera
import os.path


def test_jetson_camera():
    filename = '/data/test.jpg'
    jetson_camera_module = JetsonCamera(camera_device='csi://0')
    test_filename = '/data/test.jpg'
    jetson_camera_module.capture(filename=test_filename)
    assert os.path.exists(filename)


def test_camera_manager():
    camera_0 = JetsonCamera(camera_device='csi://0')
    camera_1 = JetsonCamera(camera_device='csi://1')
    camera_manager = CameraManager(cameras=[camera_0, camera_1])
    camera_manager.trigger(
        latitude=1.0,
        longitude=2.0,
        altitude=3.0,
        heading=1
    )
    assert True

