from tkinter import *
from PIL.ImageTk import PhotoImage
from glob import glob
import random

ruta = "images/"


def seleccion():
    nombre, foto = random.choice(imagen)
    dialogo.config(text=nombre)
    boton.config(image=foto)


root = Tk()
dialogo = Label(root, text="aquí va a ir la ruta", bg="green")
boton = Button(root, text="Presionar para ver imagen", command=seleccion)
dialogo.pack(fill=BOTH)
boton.pack()

archivo = glob(ruta + "*.jpg")
imagen = [(x, PhotoImage(file=x)) for x in archivo]
print(archivo)
root.mainloop()
