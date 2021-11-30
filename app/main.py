from time import sleep
from dronekit import connect, Vehicle
from app.camera import CameraManager
from app.multiheadcamera import MultiHeadCamera


class CameraVehicle(Vehicle):
    def __init__(self, *args):
        super(CameraVehicle, self).__init__(*args)
        output_directory = self.create_directory('/data', True)
        self.multi_head_camera = MultiHeadCamera(
            video_sources=['csi://0',
                           'csi://1'],
            output_directory=output_directory
        )
        self.gps_logger = GPSLogger(output_directory=output_directory)

        @self.on_message('CAMERA_TRIGGER')
        def listener(self, name, message):
            self.gps_logger.log(
                latitude=self.location.global_relative_frame.lat,
                longitude=self.location.global_relative_frame.lon,
                altitude=self.location.global_relative_frame.alt,
                heading=self.heading
            )
            self.multi_head_camera.capture()


if __name__ == '__main__':
    VEHICLE_CONNECTION = os.getenv("VEHICLE_CONNECTION")
    camera_vehicle = connect(
        VEHICLE_CONNECTION,
        baud=921600,
        vehicle_class=CameraVehicle
    )

    while True:
        sleep(1)
