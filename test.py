import dronekit_sitl
from time import sleep
from app import ConnectionControl


def test_prepare_events():
    sitl = dronekit_sitl.start_default()
    connection_control = ConnectionControl(sitl.connection_string())
    sleep(1)
    assert connection_control.camera_vehicle._camera.shot is True
