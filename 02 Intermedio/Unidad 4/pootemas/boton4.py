from tkinter import *
from parametrostema import bcolor, bfont, bsize
from boton1 import HolaButton


class TemaDeButton:
    def __init__(self, parent=None, **configs):

        self.myParent = parent
        self.myParent.geometry("300x300")
        button = Button(self.myParent, **configs)
        button.pack()
        button.config(bg=bcolor, font=(bfont, bsize))


def callback1():
    print("callback1")


def callback2():
    print("callback2")


class MiButton(TemaDeButton):
    def __init__(self, parent=None, **configs):
        TemaDeButton.__init__(self, parent, **configs)


if __name__ == "__main__":
    root = Tk()
    B1 = MiButton(root, text="Botón que hereda de TemaDeButton", command=callback2)
    B2 = TemaDeButton(root, text="Botón con tema y con callback1", command=callback1)
    B3 = TemaDeButton(root, text="Botón con tema y con callback2", command=callback2)
    B4 = HolaButton(root, text="Botón sin tema y con callback")
    root.mainloop()
