from tkinter import *

root = Tk()

lab1 = Label(root, text="Hello World")
lab2 = Label(root, text="New Text!")

lab1.grid(row=0, column=0)
lab2.grid(row=1, column=0)

root.mainloop()
