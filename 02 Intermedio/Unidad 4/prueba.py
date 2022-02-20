class ArtLibreria:
    def __init__(self, nombre):
        self.nombre = nombre
        print(self)

    def listado(
        self,
    ):
        print(self.nombre)


papel = ArtLibreria("Papel A4")
papel.listado()
papel2 = ArtLibreria("Papel A0")
papel2.listado()


class Personal:
    def __init__(self, nombre3, edad, sueldo=0, trabajo=None):
        self.nombre = nombre3
        self.edad = edad
        self.sueldo = sueldo
        self.trabajo = trabajo

    def incremento_sueldo(
        self,
    ):
        print(self.sueldo * 1.3)


class Gerente(Personal):
    premio = 0.30

    def incremento_sueldo(self, valor):
        print(self.sueldo * (1 + Gerente.premio + valor))
        print(round(self.sueldo * (1 + Gerente.premio + valor)))


pepe = Personal("Pepe", 67)
print(pepe.nombre)

lorena = Gerente("Lorena", 18, 50000)
hugo = Gerente("Hugo", 67, 40000)

print(lorena.premio)
print(hugo.premio)

lorena.incremento_sueldo(0.4)
hugo.incremento_sueldo(0.2)
