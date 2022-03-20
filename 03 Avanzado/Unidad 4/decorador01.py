def decorator_multiplicar_por10(funcion):
    def envoltura(*args):
        print(funcion(*args) * 10)

    return envoltura


@decorator_multiplicar_por10
def agregar(a, b):
    c = a + b
    return c


agregar(3, 5)