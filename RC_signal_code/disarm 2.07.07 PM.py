# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = int(1500 *4096/9000)  # Min pulse length out of 4096
servo_max = int(2000 *4096/9000)# Max pulse length out of 4096
n = int(1000 *4096/9000)
# Helper function to make setting a servo pulse width simpler.
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(110)


print('Moving servo on channel 0, press Ctrl-C to quit...')

# Move servo on channel O between extremes.
while True:
    pwm.set_pwm(3,0,servo_min)




    #pwm.set_pwm(2,0,servo_min)
#time.sleep(5)
#pwm.set_pwm(3, 0, servo_min)
    #pwm.set_pwm(0,0,servo_max)
##    time.sleep(1)
    #pwm.set_pwm(0, 0, servo_max)
    #time.sleep(1)



