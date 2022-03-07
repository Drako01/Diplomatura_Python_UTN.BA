import mysql.connector

# ###########################################
def crearbd():
    try:
        mibase = mysql.connector.connect(host="localhost", user="root", passwd="" )
        micursor = mibase.cursor()
        micursor.execute("CREATE DATABASE baseprueba3")
        mibase = mysql.connector.connect(host="localhost", user="root",passwd="",database="baseprueba3")
        micursor = mibase.cursor()
        micursor.execute("CREATE TABLE producto( id int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT, titulo VARCHAR(128) COLLATE utf8_spanish2_ci NOT NULL, descripcion text COLLATE utf8_spanish2_ci NOT NULL )")
        print("Base de datos con tabla creada")
        showinfo('-', 'Base de datos con tabla creada')
    except:
        print("Ya existe la base de datos")
        showinfo('-', 'Ya existe la base de datos')

def miconexion():
        
    mibase = mysql.connector.connect(host="localhost", user="root", passwd="", database="baseprueba3")
    return mibase