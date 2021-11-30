from app.camera import CameraManager
from typing import List


class MultiHead:
    def __init__(self,
                 camera_managers: List[CameraManager]):
        self.camera_managers = camera_managers
        self.__startup()

    def __startup(self):
        for cm in self.camera_managers:
            cm.startup()

    def shoot(self):
        for cm in self.camera_managers:
            cm.capture()
        for cm in self.camera_managers:
            cm.save()

    def __del__(self):
        for cm in self.camera_managers:
            cm.shutdown()
