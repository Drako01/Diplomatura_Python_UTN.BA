
import sqlite3
from sqlite3 import Error
import re


class Conectando:

    # Defino funciones para conectar y crear base de datos y tabla
    def conectar(self):
        con = sqlite3.connect("Agenda_Contacto")
        return con

    def crear_bbdd(self):
        try:
            self.conectar()
            print("Base de Dato Agenda_Contacto")
        except Error:
            print(Error)
        finally:
            self.conectar().close()

    def cursorObj(self):
        return self.conectar().cursor()

    def crear_tabla(self):
        self.cursorObj().execute(
            "CREATE TABLE IF NOT EXISTS entidad(id INTEGER PRIMARY KEY AUTOINCREMENT, DNI integer(8) NOT NULL, Apellido VARCHAR(128) NOT NULL, Nombre VARCHAR(128) NOT NULL, Direccion VARCHAR(128) NOT NULL, Localidad VARCHAR(128) NOT NULL, Telefono VARCHAR(15) NOT NULL, Email VARCHAR(128) NOT NULL)"
        )
        self.conectar().commit()
        self.conectar().close()


class control:
    def __init__(
        self,
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
    ):
        self.entrada3 = entrada3
        self.x = ingreso
        self.con = con
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.direccion = direccion
        self.localidad = localidad
        self.telefono = telefono
        self.email = email
        self.tabla = tabla

    # Definimos una Funcion para cambiar las Caracteristicas del Label
    def colorNegro(self):
        self.entrada3.config(
            fg="black", bg="LightSteelBlue", font=("Verdana", 10), width=6
        )

    def colorRojo(self):
        self.entrada3.config(
            fg="red", bg="Yellow", font=("Verdana", 10, "bold"), width=6
        )

    # Funcion para cargar un contacto
    def callback(self):
        try:
            if self.dni.get() != "":
                if self.comparar_dni() == False:
                    # Definimos la Validacion del EMail.!
                    patron = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
                    if re.match(patron, self.email.get()):
                        con = sqlite3.connect("Agenda_Contacto")
                        micursor = con.cursor()
                        sql = "INSERT INTO entidad (DNI, Apellido, Nombre, Direccion, Localidad, Telefono, EMail) VALUES (?,?,?,?,?,?,?)"
                        datos = (
                            self.dni.get(),
                            self.apellido.get(),
                            self.nombre.get(),
                            self.direccion.get(),
                            self.localidad.get(),
                            self.telefono.get(),
                            self.email.get(),
                        )
                        micursor.execute(sql, datos)
                        con.commit()
                        self.colorNegro()
                        self.x.set("Ud. Agrego al siguiente Contacto:")
                        self.tabla.insert(
                            "",
                            "end",
                            text=self.dni.get(),
                            values=[
                                self.apellido.get(),
                                self.nombre.get(),
                                self.direccion.get(),
                                self.localidad.get(),
                                self.telefono.get(),
                                self.email.get(),
                            ],
                        )
                        self.limpiar_entries()
                    else:
                        self.colorRojo()
                        self.x.set("La Direccion de Mail NO es Valida")
                else:
                    self.colorRojo()
                    self.x.set("Ya existe ese Registro")
            else:
                self.colorRojo()
                self.x.set("Ya existe ese Registro")
                print("no2")

        except:
            self.colorRojo()
            self.x.set("Ud. no ingreso ningun Dni")

    # Funcion para buscar un contacto

    def busqueda(self):
        try:
            self.micursor = self.con.cursor()
            self.sql = "SELECT * FROM entidad WHERE DNI =:documento", {
                "documento": self.dni.get()
            }
            self.micursor.execute(
                "SELECT * FROM entidad WHERE DNI =:documento",
                {"documento": self.dni.get()},
            )
            self.registro = self.micursor.fetchall()
            if not self.registro == []:
                self.limpiar_tabla()
                self.x.set(f"{self.registro}")
                i = -1
                for dato in self.registro:
                    i = i + 1
                    self.tabla.insert(
                        "", i, text=self.registro[i][1:2], values=self.registro[i][2:8]
                    )
                self.colorNegro()
                self.x.set("Se encontraron los siguientes contactos.")

            else:
                self.colorRojo()
                self.x.set("No se encontro el contacto.")
        except:
            self.colorRojo()
            self.x.set("No se encontro el contacto.")

    # Funcion para modificar un contacto

    def modificar(self):
        self.patron = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
        if re.match(self.patron, self.email.get()):
            self.micursor = self.con.cursor()
            self.colorNegro()
            sql = "UPDATE entidad SET (DNI, Apellido, Nombre, Direccion, Localidad, Telefono, EMail)=(?,?,?,?,?,?,?)WHERE DNI=?"
            dato = (
                self.dni.get(),
                self.apellido.get(),
                self.nombre.get(),
                self.direccion.get(),
                self.localidad.get(),
                self.telefono.get(),
                self.email.get(),
                self.dni.get(),
            )
            self.micursor.execute(sql, dato)
            self.con.commit()
            self.listar()
            self.limpiar_entries()
            self.x.set(
                f"Se ha modificado el Contacto DNI: {dato[0]}, de Nombre: {dato[2]} {dato[1]}"
            )
        else:
            self.colorRojo()
            self.x.set("La Direccion de Mail NO es Valida")

    # Funcion para borrar un contacto

    def borrar(self):
        self.colorNegro()
        self.fila = self.tabla.selection()

        if len(self.fila) != 0:
            self.item = self.tabla.item(self.fila)
            self.valor = int(self.item["text"])
            print(self.valor)

            self.micursor = self.con.cursor()
            sql = "DELETE FROM entidad WHERE DNI=?"
            self.micursor.execute(sql, (self.valor,))

            self.con.commit()
            self.x.set("Se ha borrado el Contacto")
            self.tabla.delete(self.fila)
            self.limpiar_entries()
        else:
            self.colorRojo()
            self.x.set("No se pudo Borrar el Contacto")

    # Funcion para cargar todos los contacto

    def listar(self):
        self.limpiar_tabla()
        self.micursor = self.con.cursor()
        self.sql = "SELECT * FROM entidad"
        self.micursor.execute(self.sql)
        self.registro = self.micursor.fetchall()

        if not self.registro == []:
            self.x.set(f"{self.registro}")
            i = -1
            for dato in self.registro:
                i = i + 1
                self.tabla.insert(
                    "", i, text=self.registro[i][1:2], values=self.registro[i][2:8]
                )
            self.colorNegro()
            self.x.set("Se encontraron los siguientes contactos.")
        else:
            self.colorRojo()
            self.x.set("No se encontro el contacto.")

    # Funcion para cargar en los entry el contacto seleccionado del treview "tabla"

    def item_elegido(
        self, tabla, dni, apellido, nombre, direccion, localidad, telefono, email
    ):
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

    def limpiar_entries(self):
        self.dni.set("")
        self.apellido.set("")
        self.nombre.set("")
        self.direccion.set("")
        self.localidad.set("")
        self.telefono.set("")
        self.email.set("")

    # Funcion para limpiar la pantalla

    def limpiar_tabla(self):
        self.x.set("")
        self.tabla.delete(*self.tabla.get_children())
        self.limpiar_entries()

    # Funcion compara DNI

    def comparar_dni(self):
        con = sqlite3.connect("Agenda_Contacto")
        self.micursor = con.cursor()
        self.micursor.execute(
            "SELECT * FROM entidad WHERE DNI =:documento", {
                "documento": self.dni.get()}
        )
        self.registro = self.micursor.fetchall()

        if not self.registro == []:
            return True
        else:
            return False
