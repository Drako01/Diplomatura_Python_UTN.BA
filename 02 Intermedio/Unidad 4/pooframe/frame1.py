from tkinter import *


class Hola(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.data = 0
        self.agregar_boton1()
        self.agregar_boton2()

    def agregar_boton1(self):
        widget = Button(self, text="Botón 1!", command=self.valor_de_variable)
        widget.pack(side=LEFT)

    def agregar_boton2(self):
        widget = Button(self, text="Botón 2!", command=self.valor_de_variable)
        widget.pack(side=LEFT)

    def valor_de_variable(self):
        self.data += 1
        print("Valor %s!" % self.data)


if __name__ == "__main__":
    Hola().mainloop()
