class Limites(object):
    __slots__ = ["edad", "sexo", "trabajo", "salario"]
    pass


x = Limites()
x.edad = 4
print(x.edad)

print("-------------------------")
x.peso = 40
print(x.peso)
