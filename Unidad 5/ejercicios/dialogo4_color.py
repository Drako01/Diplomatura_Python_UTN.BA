from tkinter import *
from tkinter.colorchooser import askcolor


def callback():
    result = askcolor(color="#00ff00", title="Bernd's Colour Chooser")
    print(result)
    print(result[1])


root = Tk()
Button(root, text="Seleccionar color", fg="green", command=callback).pack(
    side=LEFT, padx=10
)
Button(text="Cerrar", command=root.quit, fg="red").pack(side=LEFT, padx=10)
mainloop()