class ContarLlamadas:
    def __init__(self, funcion):
        self.numero_de_llamada = 0
        self.funcion = funcion

    def __call__(self, *args, **kwargs):
        self.numero_de_llamada += 1
        texto = (
            "######### NUEVA LLAMADA A FUNCIÓN: " + self.funcion.__name__ + " #########"
        )
        # print(texto ,end='!\n')
        # print('Llamada número %s a la función %s' % (self.numero_de_llamada,      self.funcion.__name__))
        self.funcion(*args, **kwargs)
        # print('----Instancia de de corador contador----')
        # print(self)
        # print('----Argumentos de función----')
        if args:
            for i in args:
                print(i)

        if kwargs:
            for clave, valor in kwargs.items():
                print("%s == %s" % (clave, valor))


@ContarLlamadas
def suma(a, b, c):
    print(a + b + c)


@ContarLlamadas
def exponencial(x, y):
    print(x ** y)


suma(1, 2, 3)
suma(a=4, b=5, c=6)
# exponencial(2,2)
# exponencial(2,6)
