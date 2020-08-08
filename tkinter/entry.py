from tkinter import *

root = Tk()

def click():
    lab = Label(root, text="hello "+e.get())
    lab.pack()

e = Entry(root, width=50)
e.pack()

but = Button(root, text="Hit me!", padx=50, command=click)
but.pack()

root.mainloop()
