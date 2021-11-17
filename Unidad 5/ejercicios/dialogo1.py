from tkinter import *
from tkinter.messagebox import *


def mensaje_error():
    showerror("Título de mensaje de error", "Contenido del mensaje de error")


def verificar():
    if askyesno("Título de la consulta de verificación", "Contenido de verificación"):
        showinfo("Si", "Mensaje de información")
    else:
        showinfo("No", "Esta a punto de salir")


Button(text="Error", command=mensaje_error).pack(fill=X)
Button(text="Verificar", command=verificar).pack(fill=X)

mainloop()