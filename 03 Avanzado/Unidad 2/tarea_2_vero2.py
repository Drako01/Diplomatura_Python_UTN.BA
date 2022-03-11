import timeit


class persona:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return "{} - Direccion: {} - Telefono: {}".format(
            self.nombre, self.direccion, self.telefono
        )


class libreta:
    __slots__ = ["nombre", "direccion", "telefono"]

    def __str__(self):
        return "{} - Direccion: {} - Telefono: {}".format(
            self.nombre, self.direccion, self.telefono
        )

def cargalibreta_nvo():
    susana = persona("Susana", "Buenos Aires", "5555-5555")

def cargalibreta():
    susana = libreta()
    susana.nombre = "Susana"
    susana.direccion = "Santa Fe"
    susana.telefono = "1111-1111"

x = timeit.timeit(lambda: cargalibreta_nvo, number=100000)
print(x)

y = timeit.timeit(lambda: cargalibreta, number=100000)
print(y)

if y < x:
    z = (y/x) * 100
    print("Utilizar Slots es un {:.0f} % mas rápido".format(z))
else:
    z = (x / y) * 100
    print("No utilizar Slots es un {:.0f} % mas rápido".format(z))
    