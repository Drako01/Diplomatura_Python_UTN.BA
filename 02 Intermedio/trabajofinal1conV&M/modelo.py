import mysql.connector
import re


# creacion de la base de datos
def crearBaseDatos():
    try:
        conexion = mysql.connector.connect(host="localhost", user="root", passwd="")
        miprimercursor = conexion.cursor()
        miprimercursor.execute("CREATE DATABASE Agenda_Contacto")
    except:
        print("La base Agenda_Contacto ya esta creada")


# Creacion de la Tabla en la Base de Datos
def crearTabla():
    conexion = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="Agenda_Contacto"
    )
    conexion.cursor().execute(
        "CREATE TABLE IF NOT EXISTS entidad( ID int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, DNI INT(8) COLLATE utf8_spanish2_ci NOT NULL, Apellido VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Nombre VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Direccion VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL , Localidad VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, Telefono VARCHAR(15) COLLATE utf8_spanish2_ci NOT NULL, Email VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL)"
    )


# Funcion para conectar a la base de datos
def conect_sql():
    mibase = mysql.connector.connect(
        host="localhost", user="root", passwd="", database="Agenda_Contacto"
    )
    return mibase


# Definimos una Funcion para cambiar las Caracteristicas del Label
def colorNegro(entrada3):
    entrada3.config(fg="black", bg="LightSteelBlue", font=("Verdana", 10), width=6)


def colorRojo(entrada3):
    entrada3.config(fg="red", bg="Yellow", font=("Verdana", 10, "bold"), width=6)


# Funcion para cargar un contacto
def callback(
    entrada3,
    x,
    con,
    dni,
    apellido,
    nombre,
    direccion,
    localidad,
    telefono,
    email,
    tabla,
):
    try:

        if comparar_dni(dni, con) == False:
            # Definimos la Validacion del EMail.!
            patron = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
            if re.match(patron, email.get()):
                micursor = con.cursor()
                sql = "INSERT INTO entidad (DNI, Apellido, Nombre, Direccion, Localidad, Telefono, EMail) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                datos = (
                    dni.get(),
                    apellido.get(),
                    nombre.get(),
                    direccion.get(),
                    localidad.get(),
                    telefono.get(),
                    email.get(),
                )
                micursor.execute(sql, datos)
                con.commit()
                colorNegro(entrada3)
                x.set("Ud. Agrego al siguiente Contacto:")
                tabla.insert(
                    "",
                    "end",
                    text=dni.get(),
                    values=[
                        apellido.get(),
                        nombre.get(),
                        direccion.get(),
                        localidad.get(),
                        telefono.get(),
                        email.get(),
                    ],
                )
                limpiar_entries(
                    dni, apellido, nombre, direccion, localidad, telefono, email
                )
            else:
                colorRojo(entrada3)
                x.set("La Direccion de Mail NO es Valida")
        else:
            colorRojo(entrada3)
            x.set("Ya existe ese Registro")
    except:
        colorRojo(entrada3)
        x.set("Ud. no ingreso ningun Dni")


# Funcion para buscar un contacto


def busqueda(
    x,
    entrada3,
    con,
    tabla,
    dni,
    apellido,
    nombre,
    direccion,
    localidad,
    telefono,
    email,
):
    try:
        micursor = con.cursor()
        sql = "SELECT * FROM entidad WHERE DNI = {}".format(dni.get())
        micursor.execute(sql)
        registro = micursor.fetchall()
        if not registro == []:
            limpiar_tabla(
                x, tabla, dni, apellido, nombre, direccion, localidad, telefono, email
            )
            x.set(f"{registro}")
            i = -1
            for dato in registro:
                i = i + 1
                tabla.insert("", i, text=registro[i][1:2], values=registro[i][2:8])
            colorNegro(entrada3)
            x.set("Se encontraron los siguientes contactos.")

        else:
            colorRojo(entrada3)
            x.set("No se encontro el contacto.")
    except:
        colorRojo(entrada3)
        x.set("No se encontro el contacto.")


# Funcion para modificar un contacto


def modificar(
    x,
    entrada3,
    con,
    tabla,
    dni,
    apellido,
    nombre,
    direccion,
    localidad,
    telefono,
    email,
):
    patron = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
    if re.match(patron, email.get()):
        micursor = con.cursor()
        colorNegro(entrada3)
        sql = "UPDATE entidad SET Apellido= %s, Nombre=%s, Direccion=%s, Localidad=%s, Telefono=%s, Email=%s WHERE DNI = %s"
        dato = (
            apellido.get(),
            nombre.get(),
            direccion.get(),
            localidad.get(),
            telefono.get(),
            email.get(),
            dni.get(),
        )
        micursor.execute(sql, dato)
        con.commit()
        listar(
            x,
            entrada3,
            con,
            tabla,
            dni,
            apellido,
            nombre,
            direccion,
            localidad,
            telefono,
            email,
        )
        limpiar_entries(dni, apellido, nombre, direccion, localidad, telefono, email)
        x.set(
            f"Se ha modificado el Contacto DNI: {dato[6]}, de Nombre: {dato[1]} {dato[0]}"
        )
    else:
        colorRojo(entrada3)
        x.set("La Direccion de Mail NO es Valida")


# Funcion para borrar un contacto


def borrar(
    x,
    entrada3,
    con,
    tabla,
    dni,
    apellido,
    nombre,
    direccion,
    localidad,
    telefono,
    email,
):
    colorNegro(entrada3)
    fila = tabla.selection()

    if len(fila) != 0:
        item = tabla.item(fila)
        valor = int(item["text"])

        micursor = con.cursor()
        sql = "DELETE FROM entidad WHERE dni = %s"
        dato = (valor,)

        micursor.execute(sql, dato)

        con.commit()
        x.set("Se ha borrado el Contacto")
        tabla.delete(fila)
        limpiar_entries(dni, apellido, nombre, direccion, localidad, telefono, email)
    else:
        colorRojo(entrada3)
        x.set("No se pudo Borrar el Contacto")


# Funcion para cargar todos los contacto


def listar(
    x,
    entrada3,
    con,
    tabla,
    dni,
    apellido,
    nombre,
    direccion,
    localidad,
    telefono,
    email,
):
    limpiar_tabla(
        x, tabla, dni, apellido, nombre, direccion, localidad, telefono, email
    )
    micursor = con.cursor()
    sql = "SELECT * FROM entidad"
    micursor.execute(sql)
    registro = micursor.fetchall()

    if not registro == []:
        x.set(f"{registro}")
        i = -1
        for dato in registro:
            i = i + 1
            tabla.insert("", i, text=registro[i][1:2], values=registro[i][2:8])
        colorNegro(entrada3)
        x.set("Se encontraron los siguientes contactos.")
    else:
        colorRojo(entrada3)
        x.set("No se encontro el contacto.")


# Funcion para cargar en los entry el contacto seleccionado del treview "tabla"


def item_elegido(tabla, dni, apellido, nombre, direccion, localidad, telefono, email):
    for selec in tabla.selection():
        item = tabla.item(selec)
        record = item["values"]
        dni.set(item["text"])
        apellido.set(record[0])
        nombre.set(record[1])
        direccion.set(record[2])
        localidad.set(record[3])
        telefono.set(record[4])
        email.set(record[5])


# Funcion para limpiar los entry


def limpiar_entries(dni, apellido, nombre, direccion, localidad, telefono, email):
    dni.set("")
    apellido.set("")
    nombre.set("")
    direccion.set("")
    localidad.set("")
    telefono.set("")
    email.set("")


# Funcion para limpiar la pantalla


def limpiar_tabla(
    ingreso, tabla, dni, apellido, nombre, direccion, localidad, telefono, email
):
    ingreso.set("")
    tabla.delete(*tabla.get_children())
    limpiar_entries(dni, apellido, nombre, direccion, localidad, telefono, email)


# Funcion compara DNI


def comparar_dni(dni, con):
    micursor = con.cursor()
    sql = "SELECT * FROM entidad WHERE DNI = {}".format(dni.get())
    micursor.execute(sql)
    registro = micursor.fetchall()

    if not registro == []:
        return True
    else:
        return False
