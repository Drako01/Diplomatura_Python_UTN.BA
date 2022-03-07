from tkinter import *
from eliminar import *
from base_datos import *

def elimina(variables, popupEliminar, elobjeto):
    popupEliminar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())

    borrar = Noticia.get(Noticia.id == lista[0])
    borrar.delete_instance()

    elobjeto.mostrar()


def eliminar(objeto):

    popupEliminar = Toplevel()
    vars_eliminar = CrearFormEliminar(popupEliminar, campos)
    
    Button(popupEliminar, text='eliminar', command=(lambda: elimina(vars_eliminar, popupEliminar, objeto))).pack()

    popupEliminar.grab_set()
    popupEliminar.focus_set()
    popupEliminar.wait_window()


