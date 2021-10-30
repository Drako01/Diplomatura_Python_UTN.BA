from tkinter import *
root = Tk()
root.config(bd=100)
e=Entry(root)
e.pack()
e.focus_set()

frutas=["Manzanas","Peras"]


texto = "Me gustan mucho las  " 

var=IntVar() 
e.config(textvariable=var)
var.set(texto+str(frutas[0])+ texto + str(frutas[1]))

mainloop()


