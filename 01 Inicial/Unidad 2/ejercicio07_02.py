from tkinter import *
root = Tk()
root.config(bd=100)
e=Entry(root)
e.pack()
e.focus_set()

frutas=["Manzanas","Peras"]


texto = "Me gustan mucho las  " 
texto1 = " pero mas me gustan las "
var=IntVar() 
e.config(textvariable=var)
var.set(texto+str(frutas[0])+ texto1 + str(frutas[1]))

mainloop()

