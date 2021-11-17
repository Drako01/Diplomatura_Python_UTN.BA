from tkinter import *

ruta = "img/"
win = Tk()
imagen = PhotoImage(file=ruta + "download.gif")
Button(win, image=imagen).pack()
win.mainloop()
