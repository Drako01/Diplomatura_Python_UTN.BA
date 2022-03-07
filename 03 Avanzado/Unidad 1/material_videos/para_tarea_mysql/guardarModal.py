from tkinter import *
from guardar import *
import base_datos
def show(variables, popupGuardar):
    popupGuardar.destroy()
    imprimir(variables)


def guarda(variables, popupGuardar, elobjeto):
    
    popupGuardar.destroy()
    print("guardar------------")
    lista = []
    for variable in variables:
        lista.append(variable.get())
    print("-----base----------------")
    mibase = base_datos.miconexion()
    print(mibase)
    print(lista)
    micursor = mibase.cursor()
    sql = "INSERT INTO producto (titulo, descripcion) VALUES (%s, %s)"
    print(sql)
    datos = (lista[0], lista[1])
    micursor.execute(sql, datos)
    mibase.commit()
    print("-------objeto----------------------------")
    elobjeto.mostrar()



def guardar(objeto):
    print("------- ver objeto -----------")
    print(objeto)
    print("------- visto objeto -----------")
    popupGuardar = Toplevel()
    vars_guardar = CrearFormGuardar(popupGuardar, campos)
    
    Button(popupGuardar, text='OK', command=(lambda: show(vars_guardar, popupGuardar))).pack()
    Button(popupGuardar, text='guardar', command=(lambda: guarda(vars_guardar, popupGuardar, objeto))).pack()

    popupGuardar.grab_set()
    popupGuardar.focus_set()
    popupGuardar.wait_window()
