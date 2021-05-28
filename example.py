from dronekit import connect
import dronekit_sitl

print("Start simulator (SITL)")

sitl = dronekit_sitl.start_default()
connection_string = sitl.connection_string()

print("Connecting to vehicle on: %s" % (connection_string,))
vehicle = connect(connection_string, wait_ready=True)

print("Get some vehicle attribute values:")
print(" GPS: %s" % vehicle.gps_0)
print(" Battery: %s" % vehicle.battery)
print(" Last Heartbeat: %s" % vehicle.last_heartbeat)
print(" Is Armable?: %s" % vehicle.is_armable)
print(" System status: %s" % vehicle.system_status.state)
print(" Mode: %s" % vehicle.mode.name)    # settable

vehicle.close()

sitl.stop()
print("Completed")
