class RaizCuadrada:
    def __init__(self, a):

        self.a = a
        self.n = len(self.a)
        self.longitud = len(self.a)

    def __iter__(self):
        # bucle for pra ordenar
        for i in range(self.n - 1):
            for j in range(self.n - 1):
                if self.a[j] > self.a[j + 1]:
                    aux = self.a[j]
                    self.a[j] = self.a[j + 1]
                    self.a[j + 1] = aux

        for valor in range(0, self.longitud):
            yield self.a[valor] ** 0.5


a = [81, 16, 64, 9]
x = RaizCuadrada(a)
p = iter(x)
print(next(p), next(p), next(p))
for i in RaizCuadrada(a):
    print(i, end=" ")
