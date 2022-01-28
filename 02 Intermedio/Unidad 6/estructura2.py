from tkinter import *


class MiApp:
    def __init__(self, parent=None, **configs):

        # ##################################################################
        # Ventana principal
        # ##################################################################
        self.my_parent = parent
        self.my_parent.geometry("700x600")

        # ##################################################################
        # Agrego contenedor
        # ##################################################################
        self.contenedor = Frame(self.my_parent, bg="#444")
        self.contenedor.pack(expand=YES, fill=BOTH)


if __name__ == "__main__":
    root = Tk()
    MiApp(root)
    root.mainloop()
