from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
#from modificacion_modulo import * 
import modificacion_modulo
from modificacion_modulo import Base_de_Datos

# Líneas para la imagen de fondo
BASE_DIR = os.path.dirname((os.path.abspath(__file__)))
ruta = os.path.join(BASE_DIR, "img", "futbol.jpg")


# Defino la ventana principal de la aplicación con su fondo
root = Tk()
image2 = Image.open(ruta)
image1 = ImageTk.PhotoImage(image2)
background_label = ttk.Label(root, image=image1)
background_label.place(x=0, y=0, relwidth=1, relheight=0.4)

# Fijo el tamaño de la ventana y el título
root.resizable(width=False, height=False)
root.title("Centro de Estadísticas del Fútbol Argentino")





# Defino función para agregar partido
def fc_insertar(con, cat, l, v, gl, gv, al, av, rl, rv,):
    ret, msg = Base_de_Datos.insertar(con, cat, l, v, gl, gv, al, av, rl, rv)
    if ret:
        fc_consultar(con, cat)
    mensaje(msg)


# Defino función para mostrar los partidos cargados de cada categoría
def fc_consultar(con, cat):
    resultado = Base_de_Datos.consultar(con, cat)
    for i in tree.get_children():
        tree.delete(i)
    for x in resultado:
        tree.insert(
            "",
            "end",
            values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9]),
        )


# Defino función para borrar registros
def fc_borrar(con):
    item_2 = tree.focus()
    item_3 = tree.item(item_2)
    if item_2:
        Base_de_Datos.borrar(con, item_3["values"][0])
        tree.delete(item_2)
        mensaje("Partido borrado!")
    else:
        mensaje("No se seleccionó registro.")


# Defino función para editar partidos
def fc_editar(con, cat, l, v, gl, gv, al, av, rl, rv):
    item_2 = tree.focus()
    item_3 = tree.item(item_2)
    cadena1 = gl
    cadena2 = gv
    if Base_de_Datos.validar_num(cadena1):
        if Base_de_Datos.validar_num(cadena2):
            if item_2:
                Base_de_Datos.editar(
                    con, cat, l, v, gl, gv, al, av, rl, rv, item_3["values"][0]
                )
                fc_consultar(con, cat)
                mensaje("Partido editado!")
            else:
                mensaje("No se seleccionó registro.")
        else:
            mensaje("Ingrese un número en el campo de goles visitante")
    else:
        mensaje("Ingrese un número en el campo de goles local")


# Defino función para cuando selecciono un item
def selectItem(a):
    item_2 = tree.focus()
    if item_2:
        item_3 = tree.item(item_2)
        e1.delete(0, END)
        e1.insert(0, item_3["values"][1])
        e2.delete(0, END)
        e2.insert(0, item_3["values"][2])
        e3.delete(0, END)
        e3.insert(0, item_3["values"][3])
        e4.delete(0, END)
        e4.insert(0, item_3["values"][4])
        e5.delete(0, END)
        e5.insert(0, item_3["values"][5])
        e6.delete(0, END)
        e6.insert(0, item_3["values"][6])
        e7.delete(0, END)
        e7.insert(0, item_3["values"][7])
        e8.delete(0, END)
        e8.insert(0, item_3["values"][8])
        e9.delete(0, END)
        e9.insert(0, item_3["values"][9])


# Defino función para notificaciones
def mensaje(texto):
    messagebox.showinfo("Atención!", texto)


# Defino función para filtrar búsqueda por equipo
def fc_filtrar(con, equipo_seleccionado):
    resultado = Base_de_Datos.filtrar(con, equipo_seleccionado)
    for i in tree.get_children():
        tree.delete(i)
    if resultado:
        for x in resultado:
            tree.insert(
                "",
                "end",
                values=(
                    x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8], x[9]
                ),
            )
    else:
        mensaje("No hay regsitros de este equipo.")



# Defino función para salir del programa
def salir():
    root.destroy()


# Llamo a las funciones para crear base de datos y tabla
Base_de_Datos.crear_bbdd("self")
con =Base_de_Datos.conectar("self")
Base_de_Datos.crear_tabla("self",con)


# Defino las variables que voy a usar
id = StringVar()
cat = ["A", "B"]
eq_a = [
    "Boca Juniors",
    "River Plate",
    "Independiente",
    "Racing",
    "San Lorenzo",
    "Estudiantes LP",
    "Gimnasia LP",
    "Newell's",
    "Rosario Central",
    "Talleres",
    "Banfield",
    "Lanús",
    "Arsenal",
    "Central Córdoba",
    "Defensa y Justicia",
    "Platense",
    "Patronato",
    "Unión",
    "Atl. Tucumán",
    "Argentinos Jrs.",
    "Colón",
    "Sarmiento",
    "Vélez",
    "Aldosivi",
    "Godoy Cruz",
    "Huracán",
]
l = StringVar()
v = StringVar()
gl = StringVar()
gv = StringVar()
al = StringVar()
av = StringVar()
rl = StringVar()
rv = StringVar()


# Creo las etiquetas, las entradas y los botones
l_cat = ttk.Label(root, text="Categoría: ")
l_l = ttk.Label(root, text="Equipo Local: ")
l_v = ttk.Label(root, text="Equipo Visitante: ")
l_gl = ttk.Label(root, text="Goles Local: ")
l_gv = ttk.Label(root, text="Goles Visitante: ")
l_al = ttk.Label(root, text="Amarillas Local: ")
l_av = ttk.Label(root, text="Amarillas Visitante: ")
l_rl = ttk.Label(root, text="Rojas Local: ")
l_rv = ttk.Label(root, text="Rojas Visitante: ")
l_x = ttk.Label(root, text="Buscar por equipo: ")

e1 = ttk.Combobox(root, values=cat, width=2)
e1.current(0)

e2 = ttk.Combobox(root, values=eq_a, width=15)
e3 = ttk.Combobox(root, values=eq_a, width=15)
e4 = ttk.Entry(root, textvariable=gl, width=2)
e5 = ttk.Entry(root, textvariable=gv, width=2)
e6 = ttk.Entry(root, textvariable=al, width=15)
e7 = ttk.Entry(root, textvariable=av, width=15)
e8 = ttk.Entry(root, textvariable=rl, width=15)
e9 = ttk.Entry(root, textvariable=rv, width=15)

ex = ttk.Combobox(root, values=eq_a, width=15)

b_agregar = ttk.Button(
    root,
    text="Insertar",
    command=lambda:fc_insertar(
        con,
        e1.get(),
        e2.get(),
        e3.get(),
        gl.get(),
        gv.get(),
        al.get(),
        av.get(),
        rl.get(),
        rv.get(),
    ),
)
b_borrar = ttk.Button(
    root, text="Borrar", command=lambda: Base_de_Datos.fc_borrar(con)
)
b_consulta_a = ttk.Button(
    root, text="Datos Cat. A", command=lambda: Base_de_Datos.fc_consultar(con, cat[0])
)
b_consulta_b = ttk.Button(
    root, text="Datos Cat. B", command=lambda: Base_de_Datos.fc_consultar(con, cat[1])
)
b_editar = ttk.Button(
    root,
    text="Editar",
    command=lambda: Base_de_Datos.fc_editar(
        con,
        e1.get(),
        e2.get(),
        e3.get(),
        gl.get(),
        gv.get(),
        al.get(),
        av.get(),
        rl.get(),
        rv.get(),
    ),
)
b_filtrar = ttk.Button(
    root, text="Buscar", command=lambda: Base_de_Datos.fc_filtrar(con, ex.get())
)
b_salir = ttk.Button(root, text="Salir", command=salir)


# Creo el treeview

style = ttk.Style(root)
style.theme_use("clam")
style.configure(
    "Treeview", background="#267830", fieldbackground="#5FE884", foreground="white"
)
style.configure(
    "Treeview.Heading",
    background="#215227",
    fieldbackground="#5FE884",
    foreground="white",
    font=("Calibri", 10, "bold"),
)
style.configure(
    "Treeview.Heading.#3",
    background="yellow",
    fieldbackground="yellow",
    foreground="black",
)
tree = ttk.Treeview(root)
tree["columns"] = ("id", "cat", "l", "v", "gl", "gv", "al", "av", "rl", "rv")
tree.column("#0", width=1, minwidth=1, anchor=W)
tree.column("id", width=30, minwidth=30)
tree.column("cat", width=100, minwidth=100, anchor=CENTER)
tree.column("l", width=120, minwidth=120)
tree.column("v", width=120, minwidth=120)
tree.column("gl", width=40, minwidth=40, anchor=CENTER)
tree.column("gv", width=40, minwidth=40, anchor=CENTER)
tree.column("al", width=100, minwidth=100)
tree.column("av", width=100, minwidth=100)
tree.column("rl", width=80, minwidth=80)
tree.column("rv", width=100, minwidth=100)

tree.heading("id", text="ID")
tree.heading("cat", text="Categoría")
tree.heading("l", text="Local")
tree.heading("v", text="Visitante")
tree.heading("gl", text="Goles Local")
tree.heading("gv", text="Goles Visita")
tree.heading("al", text="Amarillas Local")
tree.heading("av", text="Amarillas Visita")
tree.heading("rl", text="Rojas Local")
tree.heading("rv", text="Rojas Visita")

tree.bind("<ButtonRelease-1>", selectItem)


# Posiciono etiquetas, botones y controles
l_cat.grid(column=1, row=1)
l_l.grid(column=3, row=1)
l_v.grid(column=5, row=1)
l_gl.grid(column=3, row=2)
l_gv.grid(column=5, row=2)
l_al.grid(column=3, row=3)
l_av.grid(column=5, row=3)
l_rl.grid(column=3, row=4)
l_rv.grid(column=5, row=4)
l_x.grid(column=7, row=7)

e1.grid(column=2, row=1)
e2.grid(column=4, row=1)
e3.grid(column=6, row=1)
e4.grid(column=4, row=2)
e5.grid(column=6, row=2)
e6.grid(column=4, row=3)
e7.grid(column=6, row=3)
e8.grid(column=4, row=4)
e9.grid(column=6, row=4)
ex.grid(column=8, row=7)

tree.grid(column=0, row=9, columnspan=15)
b_agregar.grid(column=2, row=5, pady=10)
b_borrar.grid(column=3, row=5)
b_editar.grid(column=4, row=5)
b_consulta_a.grid(column=2, row=7)
b_consulta_b.grid(column=4, row=7)
b_filtrar.grid(column=9, row=7)
b_salir.grid(column=9, row=11)


mainloop()