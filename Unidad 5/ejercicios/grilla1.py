from tkinter import *

root = Tk()
Label(root, text="id").grid(row=0, column=0)
Label(root, text="nombre").grid(row=1, column=0)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()