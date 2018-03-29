import os
import time

attente = 3

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
    text = "test\n"
    my_type(text)

main()
