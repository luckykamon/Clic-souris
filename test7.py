import time
from pymouse import PyMouse
import pyscreenshot as ImageGrab
import webbrowser 
import imageio
import Image
import numpy as np



webbrowser.open('http://orteil.dashnet.org/cookieclicker/')

time.sleep(10)

m = PyMouse()
n=0

while True:
  time.sleep(0.003)
  m.click(244,394,1)
  n+=1
  if n>10000:
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
    time.sleep(10)
    n=0


