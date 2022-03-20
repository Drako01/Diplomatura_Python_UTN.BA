class decoratorMultiplicarPor10:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        print(self.func(*args) * 10)


@decoratorMultiplicarPor10
def agregar(a, b):
    c = a + b
    return c


agregar(3, 5)