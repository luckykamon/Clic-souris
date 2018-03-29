import os
import time

attente = 3

from pymouse import PyMouse

m = PyMouse()

m.move(500,200)
m.click(28,348,1) #cliquer

def my_type(text):
    for c in text:
        if c == " ":
            key = "KP_Space"
        elif c == "\n":
            key = "KP_Enter"
        else:
            key = c
        #
        cmd = "xdotool key {}".format(key)
        os.system(cmd)

def main():
    print("Vous avez {} secondes avant que le programme de ne se lance".format(attente))
    time.sleep(attente)
    text = "luckykamon youtube\n"
    my_type(text)

main()

time.sleep(2)

m.click(348,520,1)
