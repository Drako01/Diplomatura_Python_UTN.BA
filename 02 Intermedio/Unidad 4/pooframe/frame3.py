from tkinter import *
from frame1 import Hola


class HolaApp(Frame):
    def __init__(self, parent=None, **config):
        self.myParent = parent
        self.myParent.geometry("500x300")

        button3 = Button(self.myParent, text='Botón3')
        button3.pack()

        parent = Frame(self.myParent, bg="yellow", width=300, height=100)
        parent.pack(expand=YES, fill=X)

        Hola(self.myParent).pack(side=RIGHT)
        button4 = Button(self.myParent, text='Salir', command=exit)
        button4.pack(side=LEFT)


if __name__ == '__main__':
    root = Tk()
    miAplicacion = HolaApp(root, text='Hello subclass world')
    root.mainloop()
