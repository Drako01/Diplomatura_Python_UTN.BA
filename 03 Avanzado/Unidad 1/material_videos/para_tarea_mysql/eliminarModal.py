from tkinter import *
from eliminar import *
import base_datos

def show(variables, popupGuardar):
    popupGuardar.destroy()
    imprimir(variables)


def elimina(variables, popupEliminar, elobjeto):
    popupEliminar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())
 
    print("-----base----------------")
    mibase = base_datos.miconexion()
    print(mibase)
    print(lista)

    micursor = mibase.cursor()

    sql = "DELETE FROM producto WHERE id = %s"
    dato = (lista[0],)

    micursor.execute(sql, dato)

    mibase.commit()

    print(micursor.rowcount, "Registro borrado")
    print("-------objeto----------------------------")
    elobjeto.mostrar()






    

def eliminar(objeto):
    print("------- ver objeto -----------")
    print(objeto)
    print("------- visto objeto -----------")
    popupEliminar = Toplevel()
    vars_eliminar = CrearFormEliminar(popupEliminar, campos)
    Button(popupEliminar, text='OK', command=(lambda: show(vars_eliminar, popupEliminar))).pack()
    Button(popupEliminar, text='eliminar', command=(lambda: elimina(vars_eliminar, popupEliminar, objeto))).pack()

    popupEliminar.grab_set()
    popupEliminar.focus_set()
    popupEliminar.wait_window()


