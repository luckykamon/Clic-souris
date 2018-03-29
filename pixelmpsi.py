print "initialisation des modules en cours"
import time
from pymouse import PyMouse
import pyxhook
from random import randint

m = PyMouse()

base = []

vitesse = 58

def recup():
  def OnKeyPress(event):
    k = event.Ascii
    print k
    if k == 33: #point d'exclamation souris
      base.append(m.position())
      base.append((600+33*(randint(0,7)),700+30*randint(0,1)))
      #print m.position()
    if k == 44: #virgule fin
      new_hook.cancel()
      go(base)
  new_hook=pyxhook.HookManager()
  new_hook.KeyDown=OnKeyPress
  new_hook.HookKeyboard()
  new_hook.start()


def go(base):
    for k in base:
      if type(k) == tuple:
        m.click(k[0],k[1],1)
        time.sleep(vitesse)
    time.sleep(3) #securiter a ne pas enlever

recup()

