import os
import datetime
from typing import List
from app.camera import CameraManager


class MultiHeadCamera:
    def __init__(self,
                 video_sources: List[str],
                 output_directory: str):
        self.camera_managers = self.__create_camera_managers(video_sources,
                                                             output_directory)
        self.__startup()

    @staticmethod
    def __create_camera_managers(video_sources: List[str],
                                 output_directory: str):
        return [CameraManager(vs, output_directory) for vs in video_sources]

    def __startup(self):
        for cm in self.camera_managers:
            cm.startup()

    def capture(self):
        for cm in self.camera_managers:
            cm.capture()
        for cm in self.camera_managers:
            cm.save()

    def __del__(self):
        for cm in self.camera_managers:
            cm.shutdown()
