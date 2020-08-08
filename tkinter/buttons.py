from tkinter import *

root = Tk()

def click():
    lab = Label(root, text="I clicked!", bg="#101010", fg="#ffffff")
    lab.pack()

but = Button(root, text="Hit me!", padx=50, pady=50, command=click, bg="#101010", fg="#ffffff")
but.pack()

root.mainloop()
