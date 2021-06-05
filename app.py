import os
from time import sleep
from dronekit import connect, Vehicle


class Camera:
    def __init__(self):
        self.shot = False

    def trigger(self):
        self.shot = True


class CameraVehicle(Vehicle):
    def __init__(self, *args):
        super(CameraVehicle, self).__init__(*args)
        self._camera = Camera()

        @self.on_message('*')
        def listener(self, name, message):
            self._camera.trigger()


class ConnectionControl:
    def __init__(self, connection_string: str):
        self.camera_vehicle = connect(connection_string,
                                      vehicle_class=CameraVehicle)


if __name__ == '__main__':
    VEHICLE_CONNECTION = os.getenv("VEHICLE_CONNECTION")
    camera_control = ConnectionControl(VEHICLE_CONNECTION)

    while True:
        sleep(1)

    vehicle.close()
