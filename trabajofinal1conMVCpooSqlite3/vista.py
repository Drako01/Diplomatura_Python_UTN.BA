# Importamos las Bibliotecas de tkinter

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import modelo


class Aplicacion:
    def __init__(self, root) -> None:
        self.master = root
        # Generamos la base de datos
        self.conectado = modelo.Conectando()
        self.conectado.crear_bbdd()
        self.con = self.conectado.conectar()
        self.conectado.crear_tabla()
        """ self.conectado = modelo.conectar()
        self.conectado.crearBaseDatos()
        self.conectado.crearTabla()
        self.con = self.conectado.conect_sql() """

        # Definimos Variables
        self.colorfuente = "Black"
        self.dni = IntVar()
        self.dni.set("")
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.direccion = StringVar()
        self.localidad = StringVar()
        self.telefono = StringVar()
        self.email = StringVar()
        self.ingreso = StringVar()
        self.entidad = StringVar()
        self.imagen = PhotoImage(file="agenda2.gif")

        # llamamos a los metodos
        self.ventana()
        self.etiqueta()
        self.entry()
        self.arbol()
        self.funcionamiento()
        self.botones()

    def ventana(self):

        self.master.title(
            "Trabajo Final - Nivel Inicial - Diplomatura en Python")
        self.master.resizable(False, False)
        self.master.config(bd=20)

        # Frame donde se ubican los entry y label
        self.frame = Frame(self.master)
        self.frame.grid(row=2, column=0)
        self.frame.config(bg="LightSteelBlue")

    def etiqueta(self):
        # Encabezado de la Agenda
        Label(
            self.master,
            text="Ingrese los datos del Nuevo Contacto",
            background="LightSteelBlue",
            foreground="black",
            width=80,
        ).grid(row=0, column=0, columnspan=2, pady=10)

        # Imagen
        Label(self.master, image=self.imagen).grid(row=2, column=1, sticky=E)

        # Etiqueta con referencia a la busqueda
        Label(
            self.master,
            text="Ingrese el DNI para Buscar o Eliminar al Contacto",
            background="LightSteelBlue",
            foreground="black",
            width=80,
        ).grid(row=3, column=0, columnspan=2, pady=10)

        # En esta seccion estan los Label donde figura el Nombre de cada Campo
        Label(self.frame, text="D.N.I.", bg="LightSteelBlue").grid(
            row=2, column=0, sticky=W, pady=3, padx=6
        )
        Label(self.frame, text="Apellido", bg="LightSteelBlue").grid(
            row=3, column=0, sticky=W, pady=3, padx=6
        )
        Label(self.frame, text="Nombre(s)", bg="LightSteelBlue").grid(
            row=4, column=0, sticky=W, pady=3, padx=6
        )
        Label(self.frame, text="Dirección", bg="LightSteelBlue").grid(
            row=5, column=0, sticky=W, pady=3, padx=6
        )
        Label(self.frame, text="Localidad", bg="LightSteelBlue").grid(
            row=6, column=0, sticky=W, pady=3, padx=6
        )
        Label(self.frame, text="Telefono", bg="LightSteelBlue").grid(
            row=7, column=0, sticky=W, pady=3, padx=6
        )
        Label(self.frame, text="Correo Electronico", bg="LightSteelBlue").grid(
            row=8, column=0, sticky=W, pady=3, padx=6
        )

        # etiqueta al pie con los integrantes
        Label(
            self.master,
            text="INTEGRANTES: Alejandro Di Stefano - Oscar Quintana - Nora Nardi - Marcelo Mansilla - Juan Alberto Labajian",
            background="LightSteelBlue",
            foreground="black",
            width=100,
        ).grid(row=15, column=0, columnspan=2, pady=10)

    def entry(self):
        # En esta seccion encontramos los campos vacios correspondientes a cada Item a llenar
        Entry(self.frame, textvariable=self.dni, width=30, bd=3).grid(
            row=2, column=1, pady=3, sticky=W, padx=6
        )

        Entry(self.frame, textvariable=self.apellido, width=30, bd=3).grid(
            row=3, column=1, pady=3, sticky=W, padx=6
        )

        Entry(self.frame, textvariable=self.nombre, width=30, bd=3).grid(
            row=4, column=1, pady=3, sticky=E, padx=6
        )

        Entry(self.frame, textvariable=self.direccion, width=30, bd=3).grid(
            row=5, column=1, pady=3, sticky=W, padx=6
        )

        Entry(self.frame, textvariable=self.localidad, width=30, bd=3).grid(
            row=6, column=1, pady=3, sticky=W, padx=6
        )

        Entry(self.frame, textvariable=self.telefono, width=30, bd=3).grid(
            row=7, column=1, pady=3, sticky=W, padx=6
        )

        Entry(self.frame, textvariable=self.email, width=30, bd=3).grid(
            row=8, column=1, pady=3, sticky=W, padx=6
        )

        # entry registro de acciones del usuario
        self.entrada3 = Label(self.master, bd=4, textvariable=self.ingreso)
        self.entrada3.config(
            fg="black", bg="LightSteelBlue", font=("Verdana", 10), width=6
        )  # Foreground  # Background
        self.entrada3.grid(row=12, column=0, pady=4, columnspan=2, ipadx=300)

    def arbol(self):
        # defino la tabla donde se veran los datos
        self.tabla = ttk.Treeview(
            self.master, columns=("uno", "dos", "tres",
                                  "cuatro", "cinco", "seis")
        )
        self.tabla.column("#0", width=100, minwidth=70)
        self.tabla.column("uno", width=100, minwidth=70)
        self.tabla.column("dos", width=100, minwidth=70)
        self.tabla.column("tres", width=100, minwidth=70)
        self.tabla.column("cuatro", width=100, minwidth=70)
        self.tabla.column("cinco", width=100, minwidth=70)
        self.tabla.column("seis", width=120, minwidth=70)
        self.tabla.heading("#0", text="D.N.I", anchor="w")
        self.tabla.heading("uno", text="Apellido", anchor="w")
        self.tabla.heading("dos", text="Nombre", anchor="w")
        self.tabla.heading("tres", text="Dirección", anchor="w")
        self.tabla.heading("cuatro", text="Localidad", anchor="w")
        self.tabla.heading("cinco", text="Telefono", anchor="w")
        self.tabla.heading("seis", text="Correo Electronico", anchor="w")
        self.tabla.grid(row=14, column=0, pady=3, columnspan=2)
        self.tabla.bind(
            "<<TreeviewSelect>>",
            lambda event, a=self.tabla, b=self.dni, c=self.apellido, d=self.nombre, e=self.direccion, f=self.localidad, g=self.telefono, h=self.email: self.funcion.item_elegido(
                a, b, c, d, e, f, g, h
            ),
        )
        self.estilo = ttk.Style(self.master)
        self.estilo.theme_use("alt")
        self.estilo.configure(".", font=(
            "Helvetica", 12, "bold"), foreground="black")
        self.estilo.configure(
            "Treeview", font=("Helvetica", 10), foreground="black", background="white"
        )
        self.estilo.map(
            "Treeview",
            background=[("selected", "LightSteelBlue")],
            foreground=[("selected", "black")],
        )

    def funcionamiento(self):
        # Metodo para instanciar las funciones
        self.funcion = modelo.control(
            self.entrada3,
            self.ingreso,
            self.con,
            self.dni,
            self.apellido,
            self.nombre,
            self.direccion,
            self.localidad,
            self.telefono,
            self.email,
            self.tabla,
        )

    def botones(self):
        # Definimos el Boton de Agendado
        self.alta = Button(
            self.master,
            text="Agendar",
            command=lambda: self.funcion.callback(),
            padx=10,
            cursor="hand2",
            bd=4,
            activebackground="Royal blue",
            activeforeground="snow2",
        )
        self.alta.grid(row=9, column=0, pady=12, columnspan=1, sticky=N)

        # Definimos el Boton de Consulta

        self.buscar = Button(
            self.master,
            text="Consultar",
            command=lambda: self.funcion.busqueda(),
            padx=10,
            cursor="hand2",
            bd=4,
            activebackground="Royal blue",
            activeforeground="snow2",
        )
        self.buscar.grid(row=9, column=1, pady=12, columnspan=1, sticky=N)

        # Definimos el Boton Listar Contactos
        self.listar_ = Button(
            self.master,
            text="   Listar   ",
            command=lambda: self.funcion.listar(),
            padx=10,
            cursor="hand2",
            bd=4,
            activebackground="Royal blue",
            activeforeground="snow2",
        )
        self.listar_.grid(row=10, column=0, pady=12, columnspan=1, sticky=N)

        # Definimos el Boton de Borrar Contacto
        self.borrar_ = Button(
            self.master,
            text="   Borrar   ",
            command=lambda: self.funcion.borrar(),
            padx=10,
            cursor="hand2",
            bd=4,
            activebackground="Royal blue",
            activeforeground="snow2",
        )
        self.borrar_.grid(row=10, column=1, pady=12, columnspan=1, sticky=N)

        # Boton de Modificar Datos del Contacto
        self.modificar = Button(
            self.master,
            text="Modificar",
            command=lambda: self.funcion.modificar(),
            padx=10,
            cursor="hand2",
            bd=4,
            activebackground="Royal blue",
            activeforeground="snow2",
        )
        self.modificar.grid(row=11, column=0, pady=12, columnspan=1, sticky=N)

        # Boton de Reset Datos del Contacto
        self.reset = Button(
            self.master,
            text="    Reset    ",
            command=lambda: self.funcion.limpiar_tabla(),
            padx=10,
            cursor="hand2",
            bd=4,
            activebackground="Royal blue",
            activeforeground="snow2",
        )
        self.reset.grid(row=11, column=1, pady=12, columnspan=1, sticky=N)


"""
# Generamos la base de datos
conectado = modelo.conectar()
conectado.crearBaseDatos()
conectado.crearTabla()
con = conectado.conect_sql()

# Asignacion de la ventana

master = Tk()
master.title("Trabajo Final - Nivel Inicial - Diplomatura en Python")
master.resizable(False, False)
master.config(bd=20)

# Definimos las Funciones
colorfuente = "Black"

# Definimos Variables
dni = IntVar()
dni.set("")
nombre = StringVar()
apellido = StringVar()
direccion = StringVar()
localidad = StringVar()
telefono = StringVar()
email = StringVar()
ingreso = StringVar()
entidad = StringVar()

# Encabezado de la Agenda

encabezado = Label(
    master,
    text="Ingrese los datos del Nuevo Contacto",
    background="LightSteelBlue",
    foreground="black",
    width=80,
)
encabezado.grid(row=0, column=0, columnspan=2, pady=10)


# Imagen opcional

imagen = PhotoImage(file="agenda2.gif")
Label(master, image=imagen).grid(row=2, column=1, sticky=E)

# Etiqueta con referencia a la busqueda

encabezado = Label(
    master,
    text="Ingrese el DNI para Buscar o Eliminar al Contacto",
    background="LightSteelBlue",
    foreground="black",
    width=80,
)
encabezado.grid(row=3, column=0, columnspan=2, pady=10)

# Frame donde se ubican los entry y label

frame = Frame(master)
frame.grid(row=2, column=0)
frame.config(bg="LightSteelBlue")

# defino entrada3 y tabla por sobre la instanciacion
entrada3 = Label(master, bd=4, textvariable=ingreso)
tabla = ttk.Treeview(master, columns=("uno", "dos", "tres", "cuatro", "cinco", "seis"))

# Instancio las funciones
funcion = modelo.control(
    entrada3,
    ingreso,
    con,
    dni,
    apellido,
    nombre,
    direccion,
    localidad,
    telefono,
    email,
    tabla,
)

# Definimos el Boton de Agendado

alta = Button(
    master,
    text="Agendar",
    command=lambda: funcion.callback(),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
alta.grid(row=9, column=0, pady=12, columnspan=1, sticky=N)

# Definimos el Boton de Consulta

buscar = Button(
    master,
    text="Consultar",
    command=lambda: funcion.busqueda(),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
buscar.grid(row=9, column=1, pady=12, columnspan=1, sticky=N)

# Definimos el Boton Listar Contactos
listar_ = Button(
    master,
    text="   Listar   ",
    command=lambda: funcion.listar(),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
listar_.grid(row=10, column=0, pady=12, columnspan=1, sticky=N)

# Definimos el Boton de Borrar Contacto
borrar_ = Button(
    master,
    text="   Borrar   ",
    command=lambda: funcion.borrar(),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
borrar_.grid(row=10, column=1, pady=12, columnspan=1, sticky=N)

# Boton de Modificar Datos del Contacto
modificar = Button(
    master,
    text="Modificar",
    command=lambda: funcion.modificar(),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
modificar.grid(row=11, column=0, pady=12, columnspan=1, sticky=N)

# Boton de Reset Datos del Contacto
reset = Button(
    master,
    text="    Reset    ",
    command=lambda: funcion.limpiar_tabla(),
    padx=10,
    cursor="hand2",
    bd=4,
    activebackground="Royal blue",
    activeforeground="snow2",
)
reset.grid(row=11, column=1, pady=12, columnspan=1, sticky=N)

# En esta seccion estan los Label donde figura el Nombre de cada Campo

Label(frame, text="D.N.I.", bg="LightSteelBlue").grid(
    row=2, column=0, sticky=W, pady=3, padx=6
)
Label(frame, text="Apellido", bg="LightSteelBlue").grid(
    row=3, column=0, sticky=W, pady=3, padx=6
)
Label(frame, text="Nombre(s)", bg="LightSteelBlue").grid(
    row=4, column=0, sticky=W, pady=3, padx=6
)
Label(frame, text="Dirección", bg="LightSteelBlue").grid(
    row=5, column=0, sticky=W, pady=3, padx=6
)
Label(frame, text="Localidad", bg="LightSteelBlue").grid(
    row=6, column=0, sticky=W, pady=3, padx=6
)
Label(frame, text="Telefono", bg="LightSteelBlue").grid(
    row=7, column=0, sticky=W, pady=3, padx=6
)
Label(frame, text="Correo Electronico", bg="LightSteelBlue").grid(
    row=8, column=0, sticky=W, pady=3, padx=6
)

# En esta seccion encontramos los campos vacios correspondientes a cada Item a llenar

entrada_dni = Entry(frame, textvariable=dni, width=30, bd=3)
entrada_dni.grid(row=2, column=1, pady=3, sticky=W, padx=6)

entrada_apellido = Entry(frame, textvariable=apellido, width=30, bd=3)
entrada_apellido.grid(row=3, column=1, pady=3, sticky=W, padx=6)

entrada_nombre = Entry(frame, textvariable=nombre, width=30, bd=3)
entrada_nombre.grid(row=4, column=1, pady=3, sticky=E, padx=6)

entrada_direccion = Entry(frame, textvariable=direccion, width=30, bd=3)
entrada_direccion.grid(row=5, column=1, pady=3, sticky=W, padx=6)

entrada_localidad = Entry(frame, textvariable=localidad, width=30, bd=3)
entrada_localidad.grid(row=6, column=1, pady=3, sticky=W, padx=6)

entrada_telefono = Entry(frame, textvariable=telefono, width=30, bd=3)
entrada_telefono.grid(row=7, column=1, pady=3, sticky=W, padx=6)

entrada_email = Entry(frame, textvariable=email, width=30, bd=3)
entrada_email.grid(row=8, column=1, pady=3, sticky=W, padx=6)


# entry registro de acciones del usuario

entrada3.config(
    fg="black", bg="LightSteelBlue", font=("Verdana", 10), width=6
)  # Foreground  # Background
entrada3.grid(row=12, column=0, pady=4, columnspan=2, ipadx=300)

# defino la tabla donde se veran los datos


tabla.column("#0", width=100, minwidth=70)
tabla.column("uno", width=100, minwidth=70)
tabla.column("dos", width=100, minwidth=70)
tabla.column("tres", width=100, minwidth=70)
tabla.column("cuatro", width=100, minwidth=70)
tabla.column("cinco", width=100, minwidth=70)
tabla.column("seis", width=120, minwidth=70)

tabla.heading("#0", text="D.N.I", anchor="w")
tabla.heading("uno", text="Apellido", anchor="w")
tabla.heading("dos", text="Nombre", anchor="w")
tabla.heading("tres", text="Dirección", anchor="w")
tabla.heading("cuatro", text="Localidad", anchor="w")
tabla.heading("cinco", text="Telefono", anchor="w")
tabla.heading("seis", text="Correo Electronico", anchor="w")

tabla.grid(row=14, column=0, pady=3, columnspan=2)
tabla.bind(
    "<<TreeviewSelect>>",
    lambda event, a=tabla, b=dni, c=apellido, d=nombre, e=direccion, f=localidad, g=telefono, h=email: funcion.item_elegido(
        a, b, c, d, e, f, g, h
    ),
)

estilo = ttk.Style(master)
estilo.theme_use("alt")
estilo.configure(".", font=("Helvetica", 12, "bold"), foreground="black")
estilo.configure(
    "Treeview", font=("Helvetica", 10), foreground="black", background="white"
)
estilo.map(
    "Treeview",
    background=[("selected", "LightSteelBlue")],
    foreground=[("selected", "black")],
)

# etiqueta al pie con los integrantes

encabezado = Label(
    master,
    text="INTEGRANTES: Alejandro Di Stefano - Oscar Quintana - Nora Nardi - Marcelo Mansilla - Federico Iaccono - Juan Alberto Labajian",
    background="LightSteelBlue",
    foreground="black",
    width=100,
)
encabezado.grid(row=15, column=0, columnspan=2, pady=10)

master.mainloop()

con.close()

# fin del Programa
"""
