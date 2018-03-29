import time
from pymouse import PyMouse
import pyscreenshot as ImageGrab
import webbrowser 
import imageio
import Image
import numpy as np



webbrowser.open('http://orteil.dashnet.org/cookieclicker/')

time.sleep(5)

im=ImageGrab.grab()
im.save("screen.png")

screen = imageio.imread("screen.png")
cook = imageio.imread("cookie.png")

abscook = cook.shape[0]
ordcook = cook.shape[1]
absscreen = cook.shape[0]
ordscreen = cook.shape[1]

m = PyMouse()
n=0

while True:
  time.sleep(0.05)
  m.click(244,394,1)
  n+=1
  if n>100:
    time.sleep(0.1)
    m.click(1077,216,1)
    time.sleep(0.1)
    m.click(1211,766,1)
    time.sleep(0.1)
    m.click(1211,707,1)
    time.sleep(0.1)
    m.click(1211,649,1)
    time.sleep(0.1)
    m.click(1211,576,1)
    time.sleep(0.1)
    m.click(1211,510,1)
    time.sleep(0.1)
    m.click(1211,455,1)
    time.sleep(0.1)
    m.click(1211,455,1)
    time.sleep(0.1)
    m.click(1211,387,1)
    time.sleep(0.1)
    m.click(1211,320,1)
    time.sleep(3)
    n=0


