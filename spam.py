import pyautogui as pg

i = 0
pg.sleep(3)
while i<100 :
  pg.write("Hello world")
  pg.press("enter")
  i += 1
