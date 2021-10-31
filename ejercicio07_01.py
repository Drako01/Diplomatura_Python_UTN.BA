from tkinter import *
root = Tk()
root.config(bd=100)
e=Entry(root)
e.pack()
e.focus_set()

Lista = ["Manzana", "Frutilla","Banana", "Pera", "Kiwi", "Anana", "Uvas"]


texto = "Vamos a Imprimir por Pantalla la 3er Fruta de la Lista, y esa fruta es la "


var=IntVar() 
e.config(textvariable=var)
var.set(texto+str(Lista[2]))

mainloop()
