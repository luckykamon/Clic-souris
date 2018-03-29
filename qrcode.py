print "initialisation des modules en cours"
import sys
import os
import time
from pymouse import PyMouse
import pyxhook
from random import randint
import imageio
import matplotlib.pyplot as plt
import Image
import numpy as np

pixel = 29 #nombre de pixels de cote

m = PyMouse()

def base(image):
  pixel = 29
  fichier = open("base.txt","w")
  base = [[0 for k in range(29)] for j in range(29)]
  print base
  qrcode = imageio.imread(image)
  absc = (qrcode.shape[0])*1./pixel
  ordo = (qrcode.shape[1])*1./pixel
  for l in range(pixel):
    for c in range(pixel):
      if qrcode[int(l*absc + absc/2),int(c*ordo + ordo/2)][0]<200:
        base[l][c] = 1
  string = ""
  for v in range(len(base)):
    for w in range(len(base[v])):
      string += str(base[v][w])
  fichier.write(string)
  fichier.write("\n")
  fichier.close()

def pixel(taille):
  fichier = open("base.txt","r")
  fo = fichier.read()
  for l in range(29):
    for c in range(8,29):
      if fo[l*29+c] == "1":
        print l*29+c
        time.sleep(85)
        m.click(373+18*c,147+18*l,1)
  print "fin"
