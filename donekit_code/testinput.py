

# mode = 0
# while True: 
#   try:
#   	mode=int(input('Input:'))
#   except ValueError:
#   	print ("Not a number")
#   print (mode)

# import sys
# import threading 
# nmodule = sys.modules[__name__]
# nmodule.n = 1000


# def set_pwm():
#   number = nmodule.n
#   while True: 
#     try:
#       number=int(input('Input:'))
#     except ValueError:
#       print ("Not a number")
#     nmodule.n = number

# t2 = threading.Thread(target=set_pwm())
# t2.start()

import threading 
import time


x = 1000


class set_pwm(threading.Thread):
  def run(self):
    #print('a')
    global x
    number = x
    while True: 
      try:
        number=int(input('Input:'))
      except ValueError:
        print ("Not a number")
      x = number


class send_pwm(threading.Thread):
  def run(self):
    #print('b')
    while True:
      pn = x
      f.write(str(pn))
      f.write(' ')
      f.flush()
      time.sleep(1)


if __name__ == "__main__":
  f = open('threadpy.txt','w')


  t2 = set_pwm()
  t1 = send_pwm()

  t1.daemon = True
  t2.daemon = True
  
 
  t2.start()
  t1.start()


  t1.join()
  t2.join()

  while True:
    time.sleep(1)


