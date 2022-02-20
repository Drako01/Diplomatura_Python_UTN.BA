class Juan:

    jj = "aa"

    def __init__(self):
        super(Juan, self).__init__()


class Persona(Juan):

    jj2 = "bb"

    @classmethod
    def imprimir(cls, parametro1):
        print(parametro1 + cls.jj + cls.jj2)


Persona.imprimir("valor del parámetro 1")


input()
