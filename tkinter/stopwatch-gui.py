import time
from tkinter import *

# GUI based stopwatch

root = Tk()

stime = 0
etime = 0
i=1
def start_click():
    global stime
    stime = time.time()

def lap_click():
    global etime
    global i
    etime = time.time()
    result = ("Time: %s" % (round((etime - stime), 3)))
    Label(root, text=result).grid(row=i, column=0)
    i = i+1


stbut = Button(root, text="Start", padx=30, command=start_click) 
stbut.grid(row=0, column=0)
enbut = Button(root, text="Lap", padx=30, command=lap_click) 
enbut.grid(row=0, column=1)

root.mainloop()
