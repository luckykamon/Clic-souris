import ctypes
import windll

SetCursorPos = ctypes.windll.user32.SetCursorPos #position setting
mouse_event = ctypes.windll.user32.mouse_event #agir sur le click
 
def left_click(x, y, clicks=1): #definition de la fonction avec position et nombrede click
  SetCursorPos(x, y)
  for i in xrange(clicks):
   mouse_event(2, 0, 0, 0, 0)
   mouse_event(4, 0, 0, 0, 0)
 
left_click(200, 200)# appel de la fonction

