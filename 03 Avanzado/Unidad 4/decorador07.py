numero_de_llamada = 0


def contar_llamadas(funcion):
    def envoltura(*args, **kwargs):
        global numero_de_llamada
        numero_de_llamada += 1
        print(
            "Llamada número %s a la función %s" % (numero_de_llamada, funcion.__name__)
        )
        return funcion(*args, **kwargs)

    return envoltura


@contar_llamadas
def suma(a, b, c):
    print(a + b + c)


@contar_llamadas
def exponencial(x, y):
    print(x ** y)


suma(1, 2, 3)
suma(a=4, b=5, c=6)
exponencial(2, 2)
exponencial(2, 6)
