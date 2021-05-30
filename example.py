from time import sleep

from dronekit import connect

print("Connecting")
vehicle = connect('127.0.0.1:14551', wait_ready=True)


@vehicle.on_message('CAMERA')
def listener(self, name, message):
    print('message: %s' % message)

while True:
    sleep(1)

vehicle.close()

print("Completed")
