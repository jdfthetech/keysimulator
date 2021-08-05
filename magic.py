#!/usr/bin/python

from pynput.keyboard import Key, Controller
import time
import random

keyboard = Controller()

time.sleep(5)
#keyboard.press('1')
#keyboard.release('1')

n = 1000


for i in range(0, n-1):
    ran = random.uniform(5.2,7.4)
    keyboard.press('1')
#   time.sleep(3)
    keyboard.release('1')
    print('released 1')
    time.sleep(1)
    keyboard.press('2')
#   time.sleep(3)
    keyboard.release('2')
    print('released 2')
    time.sleep(2)
    keyboard.press('3')
    keyboard.release('3')
    print('released 3')
#   time.sleep(2)
#   keyboard.press('4')
#   keyboard.release('4')
#   time.sleep(2)
#   keyboard.press('5')
#   keyboard.release('5')            
    time.sleep(ran)

    #print(ran)
