from tkinter import *
from modificar import *
from base_datos import *


def modifica(variables, popupModificar, elobjeto):
    popupModificar.destroy()

    lista = []
    for variable in variables:
        lista.append(variable.get())

    actualizar = Noticia.update(titulo=lista[1], descripcion=lista[2]).where(
        Noticia.id == lista[0]
    )
    actualizar.execute()

    elobjeto.mostrar()


def modificar(objeto):

    popupModificar = Toplevel()
    vars_modificar = CrearFormModificar(popupModificar, campos)
    print(vars_modificar)

    Button(
        popupModificar,
        text="modificar",
        command=(lambda: modifica(vars_modificar, popupModificar, objeto)),
    ).pack()

    popupModificar.grab_set()
    popupModificar.focus_set()
    popupModificar.wait_window()
