import time
from tkinter import *

# GUI based stopwatch

root = Tk()

stime = 0
etime = 0
def start_click():
    global stime
    stime = time.time()

def end_click():
    global etime
    etime = time.time()
    result = ("Time: %s" % (round((etime - stime), 3)))
    Label(root, text=result).grid(row=1, column=0)
    # print(result)


stbut = Button(root, text="Start", command=start_click) 
stbut.grid(row=0, column=0)
enbut = Button(root, text="End", command=end_click) 
enbut.grid(row=0, column=1)

root.mainloop()


