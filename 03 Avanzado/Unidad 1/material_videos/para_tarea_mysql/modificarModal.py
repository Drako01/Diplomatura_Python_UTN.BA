from tkinter import *
from modificar import *
import base_datos

def show(variables, popupModificar):
    popupModificar.destroy()
    imprimir(variables)
    print(type(variables))


def modifica(variables, popupModificar, elobjeto):
    popupModificar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())
    print(lista)
    mibase = base_datos.miconexion()
    print(mibase)
    print(lista[0])
    print(lista[1])
    micursor = mibase.cursor()
    elid = lista[0]
    tit =lista[1]
    desc =lista[2]
    sql = "UPDATE producto SET titulo = " +"'"+ tit +"' , descripcion = " +"'"+ desc +"' WHERE id = "+ elid +""

    print(sql)
    micursor.execute(sql)
    mibase.commit()
    print("-------objeto----------------------------")
    elobjeto.mostrar()

def modificar(objeto):
    print("------- ver objeto -----------")
    print(objeto)
    print("------- visto objeto -----------")
    popupModificar = Toplevel()
    vars_modificar = CrearFormModificar(popupModificar, campos)
    print(vars_modificar)
    Button(popupModificar, text='OK', command=(lambda: show(vars_modificar, popupModificar))).pack()
    Button(popupModificar, text='modificar', command=(lambda: modifica(vars_modificar, popupModificar, objeto))).pack()

    popupModificar.grab_set()
    popupModificar.focus_set()
    popupModificar.wait_window()
