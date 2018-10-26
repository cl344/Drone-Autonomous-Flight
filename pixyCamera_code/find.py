from pixy import *
from ctypes import *
import time

# Pixy Python start#
print ("Pixy Python find IR Lock")

# Initialize Pixy Interpreter thread #
pixy_init()

class Blocks (Structure):
  _fields_ = [ ("type", c_uint),
               ("signature", c_uint),
               ("x", c_uint),
               ("y", c_uint),
               ("width", c_uint),
               ("height", c_uint),
               ("angle", c_uint) ]

blocks = BlockArray(100)


# Wait for blocks #
while 1:

  total_b = 0
  total_x = 0
  total_y = 0

  for i in range(1,20):
    count = pixy_get_blocks(100, blocks)

    if count > 0:
      # Blocks found #
      #print 'frame %3d:' % (frame)
      #frame = frame + 1
      #for index in range (0, count):
      total_x = total_x + blocks[0].x
      total_y = total_y + blocks[0].y
      total_b =  total_b+1
      
  x = -1
  y = -1

  if not total_b==0:
      x = total_x/total_b
      y = total_y/total_b
  print ("x:", x ," y:", y )
  print(" ")

      
  time.sleep(1)

