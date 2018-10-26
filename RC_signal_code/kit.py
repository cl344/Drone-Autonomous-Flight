from dronekit import *
from pymavlink import mavutil

connection_string = '/dev/ttyACM0'
baud_rate = 115200
print("Connecting to vehicle on: %s" % (connection_string))
vehicle = connect(connection_string, baud=baud_rate)

alt = vehicle.location.global_relative_frame.alt
print(alt)



