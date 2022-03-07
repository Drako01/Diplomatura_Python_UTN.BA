class Limites:
    __slots__ = ["edad", "sexo", "trabajo", "salario", "__dict__"]

    def __init__(self):
        self.d = 4


x = Limites()
print(x.d)
x.edad = 4
print(x.__dict__)
print(x.__slots__)