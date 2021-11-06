###################################
#   Autor: Alejandro Di Stefano   #
#       Funcion Factorial         #
###################################

from tkinter import *
from math import factorial
import tkinter as tk
from tkinter.colorchooser import *

master = Tk()
master.geometry("500x120")
master.title("Factorial")
master.resizable(False,False)


encabezado = Label(master, text="Funcion Factorial", background="#E0FFDA", foreground="black", width=75)
encabezado.grid(row=0, column=0, columnspan=2)

def factorial(n):   
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  

def calculate():
    result=factorial(int(entryText.get()))
    info.config(text=result)

titulo = Label(master, text="Ingrese un Numero Entero Positivo").grid(row=2, column=0, sticky=W)
ruta = Label(master, text="El Factorial del Numero Ingresado es").grid(row=4, column=0, sticky=W)

entryText = tk.Entry(text=1, bg='white', fg='black')
entryText.grid(row=2, column=1, sticky=S)
 
btn = tk.Button(master,text='Calcular', command=calculate, padx=10)
btn.grid(row=6, column=1, sticky=S)
 
info = tk.Label(text='Resultado', bg='white', fg='black')
info.grid(row=4, column=1, sticky=S)
 
master.mainloop()