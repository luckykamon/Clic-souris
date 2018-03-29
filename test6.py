import time
from pymouse import PyMouse
import pyscreenshot as ImageGrab
import webbrowser 
import imageio
import Image
import numpy as np

screen = imageio.imread("screen.png")
cook = imageio.imread("cookie.png")

abscook = cook.shape[0]
ordcook = cook.shape[1]
absscreen = cook.shape[0]
ordscreen = cook.shape[1]

def clip(a,o):
  verif = True
  for b in range(abscook/5):
    for p in range(ordcook/5):
      if not ((cook[b,p][0]-screen[a+b,o+p][0])<150 and (cook[b,p][1]-screen[a+b,o+p][1])<150 and (cook[b,p][2]-screen[a+b,o+p][2])<150):
        return False
  return True

def coordcliccook():
  for a in range(absscreen):
    for o in range(ordscreen):
      if clip(a,o):
        return [a + abscook/2, o + ordscreen/2]

a=0
m = PyMouse()
a = coordcliccook()
print a 
#m.click(a[0],a[1],1)
