from tkinter import *
master = Tk()



e = Entry(master)
e.pack()
e.focus_set()
a = 5
b = 2
c = a * b
var = IntVar()
e.config(textvariable=var)
var.set(c)


mainloop()