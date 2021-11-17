from tkinter import *

ruta = "img/"
win = Tk()
imagen = PhotoImage(file=ruta + "download.gif")
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2, 2, image=imagen, anchor=NW)
win.mainloop()
