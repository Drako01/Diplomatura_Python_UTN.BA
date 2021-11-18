from tkinter import *
from tkinter.filedialog import askopenfilename


def callback():
    ruta = askopenfilename()
    print(ruta)


Button(text="Abrir archivo", command=callback).pack(fill=X)
mainloop()