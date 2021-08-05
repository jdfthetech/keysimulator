#!/usr/bin/python

from pynput.keyboard import Key, Controller
import time
import random
from tkinter import *

keyboard = Controller()

running = True

# functions

#testclick
def clicked():

    clickLbl.configure(text="Button was clicked !!")

#ranSleep for time between each button press
def ranSleep():
    ranSleep = random.uniform(1.4,2.3)
    ranSleep = ranSleep * 1000
    # use .after(delay_ms) instead of sleep
    window.after(int(ranSleep))

#def keyPress(castTime,coolDown,keyToPress,iterNum):
#    for i in range(1, iterNum + 1):
#        startTime = coolDown * .3 + 1.2
#        endTime = startTime + .4
#        ran = random.uniform(startTime,endTime)
#        ran = ran * 1000
#        keyboard.press(keyToPress)
#        if (castTime > 0):
#            window.after(castTime * 1000 + 1000)
#        keyboard.release(keyToPress)
#        print('start time: ' + str(startTime) + ' endTime: ' + str(endTime))
#        print('key ' + str(keyToPress) + ' completed loop ' + str(i))
#        window.after(int(ran))

def keyPress(castTime,coolDown,keyToPress,iterNum):
    # sleep a few seconds after initial start button press
    window.after(5000)      
    if running:
        startTime = coolDown * .3 + 1.2
        endTime = startTime + .4
        ran = random.uniform(startTime,endTime)
        ran = ran * 1000
        keyboard.press(keyToPress)
        if (castTime > 0):
            window.after(castTime * 1000 + 1000)
        keyboard.release(keyToPress)
        print('start time: ' + str(startTime) + ' endTime: ' + str(endTime))
        print('key ' + str(keyToPress) + ' completed loop ')
        window.after(int(ran))
    window.after(1,runLoop)
        

def runLoop():  

    if (len(ct1.get()) != 0):
        coolDown1float = float(coolDown1.get())
        castTimeInt = int(ct1.get())
        iterNum = 5
        key2Press = str(key1.get())
        keyPress(castTimeInt,coolDown1float,key2Press,iterNum)



def stop():
    global running
    running = False    
    #window.after_cancel(endIt)     
    #clickLbl.configure(text="Stop Button was clicked !!")



window = Tk()
window.title("SoTA Skillups")


#sections

lbl1 = Label(window, text="Skill 1 \n   CD   ", font=("Arial Bold", 12))
coolDown1 = Entry(window,width=3)
cast1 = Label(window, text="  Cast  \n  Time  ", font=("Arial Bold", 12))
ct1 = Entry(window,width=3)
#newstuff
keylbl1 = Label(window, text="  Key  ", font=("Arial Bold", 12))
key1 = Entry(window,width=1, font=("Arial Bold", 16))

#lbl2 = Label(window, text="Skill 2 \n   CD   ", font=("Arial Bold", 12))
#coolDown2 = Entry(window,width=3)
#cast2 = Label(window, text="  Cast  \n  Time  ", font=("Arial Bold", 12))
#ct2 = Entry(window,width=3)
#key2 = '2'
#
#lbl3 = Label(window, text="Skill 3 \n   CD   ", font=("Arial Bold", 12))
#coolDown3 = Entry(window,width=3)
#cast3 = Label(window, text="  Cast  \n  Time  ", font=("Arial Bold", 12))
#ct3 = Entry(window,width=3)
#key3 = '3'
#
#lbl4 = Label(window, text="Skill 4 \n   CD   ", font=("Arial Bold", 12))
#coolDown4 = Entry(window,width=3)
#cast4 = Label(window, text="  Cast  \n  Time  ", font=("Arial Bold", 12))
#ct4 = Entry(window,width=3)
#key4 = '4'
#
#lbl5 = Label(window, text="Skill 5 \n   CD   ", font=("Arial Bold", 12))
#coolDown5 = Entry(window,width=3)
#cast5 = Label(window, text="  Cast  \n  Time  ", font=("Arial Bold", 12))
#ct5 = Entry(window,width=3)
#key5 = '5'

# grid placements

lbl1.grid(column=0, row=0)
coolDown1.grid(column=0, row=1)
cast1.grid(column=0, row=2)
ct1.grid(column=0, row=3)
#newstuff
keylbl1.grid(column=0, row=4)
key1.grid(column=0, row=5)

#lbl2.grid(column=1, row=0)
#coolDown2.grid(column=1, row=1)
#cast2.grid(column=1, row=2)
#ct2.grid(column=1, row=3)
#
#lbl3.grid(column=2, row=0)
#coolDown3.grid(column=2, row=1)
#cast3.grid(column=2, row=2)
#ct3.grid(column=2, row=3)
#
#lbl4.grid(column=3, row=0)
#coolDown4.grid(column=3, row=1)
#cast4.grid(column=3, row=2)
#ct4.grid(column=3, row=3)
#
#lbl5.grid(column=4, row=0)
#coolDown5.grid(column=4, row=1)
#cast5.grid(column=4, row=2)
#ct5.grid(column=4, row=3)

#test clicker
clickLbl = Label(window, text="Click Label", font=("Arial Bold", 12))

#sticky to left side
clickLbl.grid(column=10, row=13, sticky=W)
#lock position with .grid_propagate(False)
clickLbl.grid_propagate(False)


#btn = Button(window, text="Run Now", command=clicked)
btn = Button(window, text="Run Now", command=runLoop)
btn.grid(column=10, row=12, sticky=W)
btn.grid_propagate(False)

stopbtn = Button(window, text="Stop", command=stop)
stopbtn.grid(column=11, row=12, sticky=W)
stopbtn.grid_propagate(False)



window.geometry('640x480')
window.mainloop()



