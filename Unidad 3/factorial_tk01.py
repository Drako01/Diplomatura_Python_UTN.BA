from tkinter import *
import sys
from math import *

master = Tk()
from tkinter import ttk
master.geometry("500x120")
master.title("Factorial")
master.resizable(False,False)


encabezado = Label(master, text="Factorial de un Numero Entero", background="#E0FFDA", foreground="black", width=75)
encabezado.grid(row=0, column=0, columnspan=2)

numero = Label(master, text="Ingrese un Número").grid(row=1, column=0, sticky=W)
factorial = Label(master, text="Factorial").grid(row=2, column=0, sticky=W)


entrada_numero = Entry(master, width=25)
entrada_numero.grid(row=1, column=1)
entrada_factorial = Entry(master, width=25)
entrada_factorial.grid(row=2, column=1)


def get_selection():
      
    num = int(entrada_numero.get())
    #fact = int(entrada_factorial.set())
 
    if num > 0:
        fact = 1
        x = num
        for i in range(x):
            fact *= x
            x -= 1
            print("El Numero Ingresado es: ",entrada_numero.get(), " y su Factorial es: ", fact) 
  
    

alta = Button(master, text="Resultado", command=get_selection, padx=10)
alta.grid(row=5, column=1)


master.mainloop()
