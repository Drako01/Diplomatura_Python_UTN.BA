class limites:
    __slots__ = ["edad", "sexo", "trabajo", "salario"]

    def imprimir(self):
        print(self.edad, "ddd")


x = limites()
x.edad = 4
print(x.edad)
print(x.imprimir())

setattr(x, "sexo", "masculino")
print("-------------------------")
print(getattr(x, "edad"))
print(getattr(x, "sexo"))
