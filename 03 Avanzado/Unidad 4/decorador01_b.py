def decorator_multiplicar_por10(funcion):
    def envoltura(*args):
        print(funcion(*args) * 10)

    return envoltura


class Ejemplo:
    @decorator_multiplicar_por10
    def agregar(self, a, b):
        c = a + b
        return c


@decorator_multiplicar_por10
def agregar(a, b):
    c = a + b
    return c


agregar(3, 5)

obj1 = Ejemplo()
obj1.agregar(3, 5)