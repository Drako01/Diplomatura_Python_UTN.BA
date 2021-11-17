# ##############################################
# Pasar diccionario ############################
# ##############################################


def funcion(**kwargs):
    if kwargs is not None:
        for clave, valor in kwargs.items():
            print("%s == %s" % (clave, valor))


funcion(nombre="Juan", edad=41, sexo="Masculino")
