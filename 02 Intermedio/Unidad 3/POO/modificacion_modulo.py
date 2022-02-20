import sqlite3
from sqlite3 import Error
import re
class Base_de_Datos():
    def conectar(self):
        try:
            con = sqlite3.connect("bbdd_futbol.db")
            return con
        except Error:
            print(Error)

    def crear_bbdd(self):
        try:
            con = sqlite3.connect("bbdd_futbol.db")
        except Error:
            print(Error)
        finally:
            con.close()    

    def crear_tabla(self,con):
        cursorObj = con.cursor()
        cursorObj.execute(
            "CREATE TABLE IF NOT EXISTS partidos( id INTEGER PRIMARY KEY " + \
                "AUTOINCREMENT, categoria varchar(5) NOT NULL, local " + \
                "VARCHAR(128) NOT NULL, visitante varchar(128) NOT NULL, " + \
                "goles_local integer(3) NOT NULL, goles_visitante integer(3) " + \
                "NOT NULL, amarillas_local varchar(128), amarillas_visitante " + \
                "varchar(128), rojas_local varchar(128), rojas_visitante " + \
                "varchar(128))"
        )
    
                
    def insertar(self,con, cat, l, v, gl, gv, al, av, rl, rv):
        cadena1 = gl
        cadena2 = gv
        patron = "[0-9]"
        if re.match(patron, cadena1):
            if re.match(patron, cadena2):
                cursorObj = con.cursor()
                sql = "INSERT INTO partidos (categoria, local, visitante" + \
                    ", goles_local, goles_visitante, amarillas_local, " + \
                    "amarillas_visitante, rojas_local, rojas_visitante) " + \
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
                datos = (cat, l, v, gl, gv, al, av, rl, rv)
                cursorObj.execute(sql, datos)
                con.commit()
                return True, "Nuevo partido agregado!"
            else:
                return False, "Ingrese un número en el campo de goles visitante"
        else:
            return False, "Ingrese un número en el campo goles local"
    

    def consultar(self,con, cat):
        try:
            cursorObj = con.cursor()
            cursorObj.execute("SELECT * FROM partidos WHERE categoria=?", cat)
            return cursorObj.fetchall()
        except:
            print("No se pudo realizar la consulta")

    def borrar(self,con, id_borrar):
        cursorObj = con.cursor()
        sql = "DELETE FROM partidos WHERE id=?"
        cursorObj.execute(sql, (id_borrar,))
        con.commit()

    def filtrar(self,con, equipo_seleccionado):
        try:
            cursorObj = con.cursor()
            cursorObj.execute(
                "SELECT * FROM partidos WHERE local=? OR visitante=?",
                (equipo_seleccionado, equipo_seleccionado),
            )
            return cursorObj.fetchall()

        except:
            print("No se pudo realizar la consulta")

    def editar(self,con, cat, l, v, gl, gv, al, av, rl, rv, id_seleccionado):
        cursorObj = con.cursor()
        sql = "UPDATE partidos SET (categoria, local, visitante, goles_local, " + \
            "goles_visitante, amarillas_local, amarillas_visitante, " + \
            "rojas_local, rojas_visitante)=(?, ?, ?,?, ?, ?, ?, ?, ?) WHERE id=?"
        datos = (cat, l, v, gl, gv, al, av, rl, rv, id_seleccionado)
        cursorObj.execute(sql, datos)
        con.commit()

    def validar_num(self,cadena):
        return re.match("[0-9]", cadena)
    
conexion=Base_de_Datos()    
    