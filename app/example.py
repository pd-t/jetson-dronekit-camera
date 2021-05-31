from time import sleep

from dronekit import connect

import dronekit_sitl

sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

print("Connecting")
vehicle = connect(connection_string, wait_ready=True)


@vehicle.on_message('*')
def listener(self, name, message):
    print('message: %s' % message)

while True:
    sleep(1)

vehicle.close()

print("Completed")
