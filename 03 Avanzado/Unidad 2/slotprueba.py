class Limites(object):
    __slot__ = ["edad", "sexo", "trabajo", "salario"]

    def imprimir(self):
        print(self.edad, "ddd")


x = Limites()
x.edad = 4
print(x.edad)
print(x.imprimir())

setattr(x, "sexo", "masculino")
print("-------------------------")
print(getattr(x, "edad"))
print(getattr(x, "sexo"))

print("-------------------------")
x.peso = 40