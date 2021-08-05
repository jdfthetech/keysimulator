#!/usr/bin/python

from pynput.keyboard import Key, Controller
import time
import random
from tkinter import *

keyboard = Controller()

window = Tk()
window.title("Key Press Automator")

clicked_stop = BooleanVar()
clicked_stop.set(False)

current = None

###FUNCTIONS###

#test button notifier
def clicked():
    clickLbl.configure(text="Button was clicked !!")

#ranSleep for time between each button press
def ranSleep():
    ranSleep = random.uniform(1.4,2.3)
    ranSleep = ranSleep * 1000
    # use .after(delay_ms) instead of sleep
    window.after(int(ranSleep))

def keyPress(castTime,coolDown,keyToPress,iterNum):
    global current
    if clicked_stop.get() == True:
        window.after_cancel(current)
    else:
        startTime = coolDown * .3 + 1.2
        endTime = startTime + .4
        ran = random.uniform(startTime,endTime)
        ran = ran * 1000
        window.after(int(ran))
        keyboard.press(keyToPress)
        if (castTime > 0):
            window.after(castTime * 1000 + 1000)
        keyboard.release(keyToPress)
        print('start time: ' + str(startTime) + ' endTime: ' + str(endTime))
        print('key ' + str(keyToPress) + ' completed loop ')
        current = window.after(50, runLoop)
        
    



def runLoop():  
    
    if (len(ct1.get()) == 1):
        coolDown1float = float(coolDown1.get())
        castTimeInt = int(ct1.get())
        iterNum = 1000
        key2Press = str(key1.get())
        keyPress(castTimeInt,coolDown1float,key2Press,iterNum)
    if (len(ct2.get()) == 1):
        coolDown2float = float(coolDown2.get())
        castTimeInt = int(ct2.get())
        iterNum = 1000
        key2Press = str(key2.get())
        keyPress(castTimeInt,coolDown2float,key2Press,iterNum)
    if (len(ct3.get()) == 1):
        coolDown3float = float(coolDown3.get())
        castTimeInt = int(ct3.get())
        iterNum = 1000
        key2Press = str(key3.get())
        keyPress(castTimeInt,coolDown3float,key2Press,iterNum)
    if (len(ct4.get()) == 1):
        coolDown4float = float(coolDown4.get())
        castTimeInt = int(ct4.get())
        iterNum = 1000
        key2Press = str(key4.get())
        keyPress(castTimeInt,coolDown4float,key2Press,iterNum)
    if (len(ct5.get()) == 1):
        coolDown5float = float(coolDown5.get())
        castTimeInt = int(ct5.get())
        iterNum = 1000
        key2Press = str(key5.get())
        keyPress(castTimeInt,coolDown5float,key2Press,iterNum)
    

def start():
    # try this for cancel button
    global running
    running = True  
    window.after(10000)
    if (len(ct1.get()) == 1):
        coolDown1float = float(coolDown1.get())
        castTimeInt = int(ct1.get())
        iterNum = 1000
        key2Press = str(key1.get())
        keyPress(castTimeInt,coolDown1float,key2Press,iterNum)

def stop():
    clicked_stop.set(True)

###END FUNCTIONS###    

#widgets
lbl1 = Label(window, text="Skill 1 \n   CD   ", font=("Arial Bold", 12))
coolDown1 = Entry(window,width=3)
cast1 = Label(window, text="  Cast  \n  Time  ", font=("Arial Bold", 12))
ct1 = Entry(window,width=3)
keylbl1 = Label(window, text="  Key  ", font=("Arial Bold", 12))
key1 = Entry(window,width=1, font=("Arial Bold", 16))

lbl2 = Label(window, text="Skill 2 \n   CD   ", font=("Arial Bold", 12))
coolDown2 = Entry(window,width=3)
cast2 = Label(window, text="  Cast  \n  Time  ", font=("Arial Bold", 12))
ct2 = Entry(window,width=3)
keylbl2 = Label(window, text="  Key  ", font=("Arial Bold", 12))
key2 = Entry(window,width=1, font=("Arial Bold", 16))

lbl3 = Label(window, text="Skill 3 \n   CD   ", font=("Arial Bold", 12))
coolDown3 = Entry(window,width=3)
cast3 = Label(window, text="  Cast  \n  Time  ", font=("Arial Bold", 12))
ct3 = Entry(window,width=3)
keylbl3 = Label(window, text="  Key  ", font=("Arial Bold", 12))
key3 = Entry(window,width=1, font=("Arial Bold", 16))

lbl4 = Label(window, text="Skill 4 \n   CD   ", font=("Arial Bold", 12))
coolDown4 = Entry(window,width=3)
cast4 = Label(window, text="  Cast  \n  Time  ", font=("Arial Bold", 12))
ct4 = Entry(window,width=3)
keylbl4 = Label(window, text="  Key  ", font=("Arial Bold", 12))
key4 = Entry(window,width=1, font=("Arial Bold", 16))

lbl5 = Label(window, text="Skill 5 \n   CD   ", font=("Arial Bold", 12))
coolDown5 = Entry(window,width=3)
cast5 = Label(window, text="  Cast  \n  Time  ", font=("Arial Bold", 12))
ct5 = Entry(window,width=3)
keylbl5 = Label(window, text="  Key  ", font=("Arial Bold", 12))
key5 = Entry(window,width=1, font=("Arial Bold", 16))


# placements with grid
lbl1.grid(column=0, row=0)
coolDown1.grid(column=0, row=1)
cast1.grid(column=0, row=2)
ct1.grid(column=0, row=3)
keylbl1.grid(column=0, row=4)
key1.grid(column=0, row=5)


lbl2.grid(column=1, row=0)
coolDown2.grid(column=1, row=1)
cast2.grid(column=1, row=2)
ct2.grid(column=1, row=3)
keylbl2.grid(column=1, row=4)
key2.grid(column=1, row=5)
#
lbl3.grid(column=2, row=0)
coolDown3.grid(column=2, row=1)
cast3.grid(column=2, row=2)
ct3.grid(column=2, row=3)
keylbl3.grid(column=2, row=4)
key3.grid(column=2, row=5)
#
lbl4.grid(column=3, row=0)
coolDown4.grid(column=3, row=1)
cast4.grid(column=3, row=2)
ct4.grid(column=3, row=3)
keylbl4.grid(column=3, row=4)
key4.grid(column=3, row=5)
#
lbl5.grid(column=4, row=0)
coolDown5.grid(column=4, row=1)
cast5.grid(column=4, row=2)
ct5.grid(column=4, row=3)
keylbl5.grid(column=4, row=4)
key5.grid(column=4, row=5)

#test clicker
clickLbl = Label(window, text="Click Label", font=("Arial Bold", 12))

#sticky to left side
clickLbl.grid(column=10, row=13, sticky=W)
#lock position with .grid_propagate(False)
clickLbl.grid_propagate(False)


#btn = Button(window, text="Run Now", command=clicked)
btn = Button(window, text="Run Now", command=start)
btn.grid(column=10, row=12, sticky=W)
btn.grid_propagate(False)

stopbtn = Button(window, text="Stop", command=stop)
stopbtn.grid(column=11, row=12, sticky=W)
stopbtn.grid_propagate(False)





window.geometry('640x480')
window.mainloop()        