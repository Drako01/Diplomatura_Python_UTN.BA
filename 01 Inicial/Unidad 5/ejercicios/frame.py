from tkinter import *

master = Tk()

Label(text="uno").pack()
separador = Frame(height=2, bd=1, relief=SUNKEN)
separador.pack(fill=X, padx=5, pady=5)
Label(text="dos").pack()

mainloop()