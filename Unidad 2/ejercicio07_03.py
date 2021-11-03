from tkinter import *
root = Tk()
root.config(bd=100)
e=Entry(root)
e.pack()
e.focus_set()


diccionario= {'Identificador': 'valor1', 'Nombre':'valor2', 'Apellido':'valor3', 'Telefono':'valor4'}

n_base = len(diccionario)  
n_base = str(n_base)  
v_claves = list(diccionario.keys()) 
v_claves = " - ".join(v_claves) 

texto = "El numero de Elementos del Diccionario es: " 
texto01 = " y Las Claves del Diccionario son: "
c = texto + n_base + texto01 + v_claves

mensaje = Label(e, text=c)
mensaje.grid(row=1, column=2, columnspan=2)

var = IntVar()
e.config(textvariable=var)
var.set(c)

mainloop()

