from tkinter import *
from boton1 import HolaButton


class TemaDeButton():
    def __init__(self, parent=None, **configs):

        self.myParent = parent
        self.myParent.geometry("300x300")
        button = Button(self.myParent, **configs)
        button.pack()
        button.config(fg='black', bg='yellow', font=('courier', 12),
        relief=RAISED, bd=5)

def callback2():
    print('callback2')

if __name__ == '__main__':
    root = Tk()
    B1 = TemaDeButton(root, text='Botón con tema y con callback',
    command= callback2)
    B2 = TemaDeButton(root, text='Botón con tema y sin callback')
    B3 = HolaButton(root, text='Botón sin tema')

    root.mainloop()