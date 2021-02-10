""" EE 250L Lab 02: GrovePi Sensors

List team members here.

Insert Github repository link here.

link to repo: https://github.com/usc-ee250-spring2021/lab02-johnheo1128 
link to video demo: https://drive.google.com/file/d/1bB0rB0y8Eu4QCs3bQ8dO828X6LQB_jmq/view?usp=sharing
"""
"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import *
"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
setRGB(0,255,0)
if __name__ == '__main__':

  #Connect ultrasounic sensor to D4
  ultrasonic = 4
  #Connect rotary angle sensor to A2
  potentiometer = 2 
  while True:
    #So we do not poll the sensors too quickly which may introduce noise,
    #sleep for a reasonable time of 200ms between each iteration.
    time.sleep(0.2)
    # Read from potentiometer
    threshold = grovepi.analogRead(potentiometer)
    # Read distance value from Ultrasonic
    distance = grovepi.ultrasonicRead(ultrasonic)

    thr = str(threshold)
    dist = str(distance)
    if distance < threshold: #object detected!
      setText_norefresh(thr + "cm " + "OBJ PRES  \n" + dist + "cm ")
      setRGB(255,0,0)
    else:
      setText_norefresh(thr + "cm " + "          \n" + dist + "cm ")
      setRGB(0,255,0)
    #print("thresh: " + thr + "\n")
    #print("dist: " + dist + "\n\n")
    



