from tkinter import *

root = Tk()
e = Entry(root)
e.pack()
e.focus_set()
var = StringVar()
e.config(textvariable=var)
var.set("1234567")
e.icursor(4)


def callback():
    print(e.get())


b = Button(root, text="get", width=10, command=callback)
b.pack()
mainloop()
