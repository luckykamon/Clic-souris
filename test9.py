print "initialisation des modules en cours"
import sys
import os
import time
from pymouse import PyMouse
import pyxhook
from random import randint

m = PyMouse()

base = []

vitesse = 58

def depart(s):
  while s>0:
    print s
    time.sleep(1)
    s -= 1

def my_type(text):
    for c in text:
        if c == " ":
            key = "KP_Space"
        elif c == "\n":
            key = "KP_Enter"
        else:
            key = c
        cmd = "xdotool key {}".format(key)
        os.system(cmd)

def recup():
  def OnKeyPress(event):
    k = event.Ascii
    print k
    if 97 <= k <= 122: #lettre
      base.append(k)
      #print "lettre"
    if (k == 38 or k == 233 or k == 34 or k == 39 or k == 40 or k ==45  or k == 232 or k == 95 or k == 231): #chiffre
      base.append(k)
      #print "chiffre"
    if k == 33: #point d'exclamation souris
      base.append(m.position())
      #print m.position()
    if k == 32: #space
      base.append(32)
      #print "space"
    if k == 44: #virgule fin
      new_hook.cancel()
      go(base)
  new_hook=pyxhook.HookManager()
  new_hook.KeyDown=OnKeyPress
  new_hook.HookKeyboard()
  new_hook.start()


def go(base):
  while True:
    for k in base:
      if k == 32:
        time.sleep(vitesse)
        l = "KP_Space"
        cmd = "xdotool key {}".format(l)
        os.system(cmd)
      if (type(k) == int and 49 <= k <= 57):
        time.sleep(vitesse)
        depart(k-48)
      if (type(k) == int and 97 <= k <= 122):
        time.sleep(vitesse)
        l = chr(k)
        cmd = "xdotool key {}".format(l)
        os.system(cmd)
      if type(k) == tuple:
        time.sleep(vitesse)
        m.click(k[0],k[1],1)
      if (k == 38 or k == 233 or k == 34 or k == 39 or k == 40 or k ==45  or k == 232 or k == 95 or k == 231):
        time.sleep(vitesse)
        l = number(k)
        depart(l)
    time.sleep(3)

def number(k):
  if k == 38:
    return 1
  if k == 233:
    return 2
  if k == 34:
    return 3
  if k == 39:
    return 4
  if k == 40:
    return 5
  if k == 45:
    return 6
  if k == 232:
    return 7
  if k == 95:
    return 8
  if k == 231:
    return 9


print "Chaque appuie de la barre d'espace enregistrera un clic espace de [vitesse] secondes avec le suivant. Pour augmenter ce laps de temps entre chaque clic, appuyez sur les chiffres de 1 a 9, ce chiffre augmentera en seconde le temps de pause du programme. Pour enregistrer des frappes de touche, il faudra appuyer sur les touches, ps: les touches de l'alphabet"
depart(1)
recup()

