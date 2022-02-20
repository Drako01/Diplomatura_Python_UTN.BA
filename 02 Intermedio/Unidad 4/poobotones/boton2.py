from tkinter import *
from boton1 import HolaButton

class MiButton(HolaButton):
    def callback(self):
        print("Texto modificado!...")

if __name__ == '__main__':
    root = Tk()
    root.geometry("300x200")
    MiButton(root, text='Botón de subclase')
    root.mainloop()
