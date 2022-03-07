class ClasePadre:
    atributo1 = "rojo"

    def Metodo1(self):
        pass


class ClaseHija(ClasePadre):

    atributo1 = "azul"

    def metodo1(self):
        pass


X = ClaseHija()
print(X.__dict__)  # Diccionario vacío correspondiente al namespace
print(X.__class__)
print(ClaseHija.__bases__)
print(ClasePadre.__bases__)
print(list(ClaseHija.__dict__.keys()))
print(list(ClasePadre.__dict__.keys()))
