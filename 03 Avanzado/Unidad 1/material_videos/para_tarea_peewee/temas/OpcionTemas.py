import shelve


# ##################################################################
# Defino base de datos
# ##################################################################
with shelve.open("temas/OpcionTemas") as db:
    db["tema1"] = "#056E5C"
    db["tema2"] = "#1C1AE8"
    db["tema3"] = "#E80F00"

# ##################################################################
# Defino comando para modificar propiedades de los temas
# ##################################################################

def EleccionTema (variable):
    with shelve.open("temas/OpcionTemas") as db:
        if variable == 0:
            variable = "tema1"
        elif variable == 1:
            variable = "tema2"
        elif variable == 2:
            variable = "tema3"
        TemaSeleccionado = db[variable]
        return TemaSeleccionado



