from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image


import os

BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, "img")
ruta = STATIC_ROOT + "\\mascotas.jpg"
print("-------------")
print(BASE_DIR)
print(STATIC_ROOT)
print(ruta)
print("-------------")


app = Tk()
app.title("Hola S.O")
image2 = Image.open(ruta)
print(image2)
image1 = ImageTk.PhotoImage(image2)
print(image1)
background_label = tk.Label(app, image=image1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
app.mainloop()