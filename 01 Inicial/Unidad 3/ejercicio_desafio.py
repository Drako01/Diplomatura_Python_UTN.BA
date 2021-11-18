###################################
#   Autor: Alejandro Di Stefano   #
#       Ejercicio Desafio         #
###################################

from tkinter import *

master = Tk()
master.geometry("550x120")
master.title("Tarea POO")
master.resizable(False,False)


encabezado = Label(master, text="Ingrese sus datos", background="#E0FFDA", foreground="black", width=75)
encabezado.grid(row=0, column=0, columnspan=3)

titulo = Label(master, text="Título").grid(row=1, column=0, sticky=W)
ruta = Label(master, text="Ruta").grid(row=2, column=0, sticky=W)
descripcion = Label(master, text="Descripción").grid(row=3, column=0, sticky=W)

entrada_titulo = Entry(master, width=25)
entrada_titulo.grid(row=1, column=1)
entrada_ruta = Entry(master, width=25)
entrada_ruta.grid(row=2, column=1)
entrada_descripcion = Entry(master, width=25)
entrada_descripcion.grid(row=3, column=1)


def callback():
    print("Nueva alta de datos")
    print(entrada_titulo.get(), entrada_ruta.get(), entrada_descripcion.get())


def colorchange():
    color = master.config(bg="#A3FF91")
    entrada_titulo = Entry(master, width=25,bg="Green")
    entrada_titulo.grid(row=1, column=1)    
    entrada_ruta = Entry(master, width=25,bg="Green")
    entrada_ruta.grid(row=2, column=1)
    entrada_descripcion = Entry(master, width=25,bg="Green")
    entrada_descripcion.grid(row=3, column=1)

    return color


alta = Button(master, text="Imprimir", command=callback, padx=10)
alta.grid(row=4, column=1)
sorpresa = Button(master, text="Sorpresa", command=colorchange, padx=20)
sorpresa.grid(row=4, column=2, sticky=W)

master.mainloop()
