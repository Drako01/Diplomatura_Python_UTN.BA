from tkinter import *
from tkinter.messagebox import *

root = Tk()
root.title("Mi aplicación")


def hola():
    print("Hola!")


menubar = Menu(root)

# Elemento desplegable “Archivo”
menuArchivo = Menu(menubar, tearoff=0)
menuArchivo.add_command(label="Abrir", command=hola)
menuArchivo.add_command(label="Guardar", command=hola)
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label="Archivo", menu=menuArchivo)

# Elemento desplegable “Editar”
menuEdicion = Menu(menubar, tearoff=True)
menuEdicion.add_command(label="Cortar", command=hola)
menuEdicion.add_command(label="Copiar", command=hola)
menuEdicion.add_command(label="Pegar", command=hola)
menuEdicion.add_separator()
menubar.add_cascade(label="Editar", menu=menuEdicion)

submenu = Menu(menuEdicion, tearoff=True)
submenu.add_command(label="Rotar", command=hola)
submenu.add_command(label="Deformación libre", command=hola)
menuEdicion.add_cascade(label="Transformación", menu=submenu)

# Elemento desplegable “Ayuda”
menuAyuda = Menu(menubar, tearoff=0)
menuAyuda.add_command(label="Acerca de..", command=hola)
menubar.add_cascade(label="Ayuda", menu=menuAyuda)

# Mostrar menú
root.config(menu=menubar)

root.mainloop()
