import os
from time import sleep

from dronekit import connect, Vehicle

from app.camera_manager import CameraManager
from app.jetson_camera import JetsonCamera


class CameraVehicle(Vehicle):
    def __init__(self, *args):
        super(CameraVehicle, self).__init__(*args)
        camera_0 = JetsonCamera(camera_device='csi://0')
        camera_1 = JetsonCamera(camera_device='csi://1')

        @self.on_message('CAMERA_TRIGGER')
        def listener(self, name, message):
            self.camera_manager.trigger(
                latitude=self.location.global_relative_frame.lat,
                longitude=self.location.global_relative_frame.lon,
                altitude=self.location.global_relative_frame.alt,
                heading=self.heading
            )


if __name__ == '__main__':
    VEHICLE_CONNECTION = os.getenv("VEHICLE_CONNECTION")
    camera_vehicle = connect(
        VEHICLE_CONNECTION,
        baud=921600,
        vehicle_class=CameraVehicle
    )

    while True:
        sleep(1)
