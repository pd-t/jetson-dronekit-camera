from typing import List
from multiprocessing import Process

from app.jetson_camera import JetsonCamera


class CameraManager:
    def __init__(
            self,
            cameras: List[JetsonCamera]
    ):
        self.cameras = cameras

    def trigger(
            self,
            latitude: float,
            longitude: float,
            altitude: float,
            heading: int
    ):
        proc = []
        for cam, index in zip(self.cameras,
                              range(len(self.cameras))):
            filename = '/data/cam' + str(index) + '.jpg'
            p = Process(target=cam.capture, args=(filename,))
            proc.append(p)
        for p in proc:
            p.start()
        for p in proc:
            p.join()
