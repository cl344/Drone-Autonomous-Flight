from dronekit import *
from  pymavlink import mavutil
import time
import signal

str = '/dev/ttyACM0'
br = 115200

vehicle = connect(str,baud=br)
while True:
    print(vehicle.location.global_relative_frame.alt)
    time.sleep(1)
    
def out(*args):
    vehicle.close()
    quit()
    
signal.signal(signal.SIGINT,out)


