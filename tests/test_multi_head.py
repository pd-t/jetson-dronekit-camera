from app.camera import CameraManager
from app.multihead import MultiHead
from time import sleep


def test_multi_head():
    csi0 = CameraManager(video_source='csi://0',
                         video_output='file:///data/cam0_%i.jpg')

    csi1 = CameraManager(video_source='csi://1',
                         video_output='file:///data/cam1_%i.jpg')

    multi_head = MultiHead(camera_managers=[csi0, csi1])

    for i in range(3):
        multi_head.shoot()
        sleep(1)

    del multi_head
