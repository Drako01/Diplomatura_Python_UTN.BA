from tkinter import *

root = Tk()
root.geometry("380x400")
canvas = Canvas(root, width=525, height=300, bg="white")
canvas.pack(expand=YES, fill=BOTH)
########################################################
# Agregar imagen
########################################################
photo = PhotoImage(file="img/pera.gif")
canvas.create_image(0, 0, image=photo, anchor=NW)

########################################################
# Crear un conjunto de líneas
# range(inicio, fin, paso)
########################################################
for i in range(2, 12, 3):
    canvas.create_line(130, 250 + i, 200, 250 + i)
    print(i)
########################################################
# Crear un ovalo
########################################################
canvas.create_oval(70, 100, 140, 200, width=2, fill="blue")
canvas.create_oval(80, 140, 120, 200, width=2, fill="white")
canvas.create_oval(90, 160, 110, 180, width=2, fill="black")

########################################################
# Crear un rectangulo
########################################################
canvas.create_rectangle(200, 100, 300, 200, width=5, fill="green")
########################################################
# Crear una línea
########################################################
canvas.create_line(200, 100, 300, 200, width=3, fill="OrangeRed")
########################################################
# Crear un poligono
########################################################
canvas.create_polygon(165, 165, 155, 220, 180, 220, width=2, fill="green")
########################################################
# Crear un arco
########################################################
canvas.create_arc(
    60, 60, 140, 100, start=0, extent=210, outline="#f11", fill="#1f1", width=2
)
canvas.create_arc(
    200, 60, 280, 100, start=-20, extent=200, outline="#f11", fill="#1f1", width=2
)

########################################################
# Agregar Label
########################################################
widget = Label(canvas, text="Label", fg="white", bg="black")
widget.pack()
########################################################
# Agregar texto
########################################################
canvas.create_text(162, 35, text="Soy un robot")

mainloop()
