import time,random
import pyautogui as pg

msg = ("P","L","R")
time.sleep(1P)


for i in range(10):
    a = random.choice(msg)
    pg.write(a)
    pg.press("enter")
