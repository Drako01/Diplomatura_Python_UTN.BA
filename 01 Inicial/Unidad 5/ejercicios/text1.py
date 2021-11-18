from tkinter import *

root = Tk()
# La altura da la cantidad de líneas
# El ancho da la cantidad de caracteres
T = Text(root, height=4, width=33)
T.pack()
texto1 = """
1.-Línea 1--------------------
\n2.-Línea 2------------------
\n3.-Línea 3------------------
\n4.-Línea 4------------------
\n5.-Línea 5------------------
\n6.-Línea 6------------------
"""
T.insert(END, texto1)
mainloop()
