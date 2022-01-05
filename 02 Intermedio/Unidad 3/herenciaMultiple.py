class Clase1():
    def tipo(self):
        print("Soy clase1")


class Clase2a(Clase1):
    def tipo(self):
        print("Soy clase2a")


class Clase2b(Clase1):
    def tipo(self):
        print("Soy clase2b")


class Clase3(Clase2a, Clase2b):
    def tipo(self):
        print("Soy clase3")


print(Clase3.__mro__)




input()
