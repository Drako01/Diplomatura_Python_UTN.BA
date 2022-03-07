from tkinter import *
from guardar import *
from base_datos import *

def guarda(variables, popupGuardar, elobjeto):
    
    popupGuardar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())
    noticia = Noticia()
    noticia.titulo = lista[0]
    noticia.descripcion = lista[1]
    noticia.save()
    elobjeto.mostrar()



def guardar(objeto):

    popupGuardar = Toplevel()
    vars_guardar = CrearFormGuardar(popupGuardar, campos)
    
    Button(popupGuardar, text='guardar', command=(lambda: guarda(vars_guardar, popupGuardar, objeto))).pack()

    popupGuardar.grab_set()
    popupGuardar.focus_set()
    popupGuardar.wait_window()
