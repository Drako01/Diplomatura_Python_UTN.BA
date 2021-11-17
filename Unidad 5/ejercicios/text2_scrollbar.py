from tkinter import *

root = Tk()
S = Scrollbar(root)
T = Text(root, height=4, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
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
