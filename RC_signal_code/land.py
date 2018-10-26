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



# Helper function to make setting a servo pulse width simpler.
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(110)


num = 2000
n = int(num *4096/9000)
n2 = int(1000 *4096/9000)
print('Moving servo on channel 0, press Ctrl-C to quit...')
while True:
    pwm.set_pwm(4, 0, n)
    pwm.set_pwm(2, 0, n2)
   


