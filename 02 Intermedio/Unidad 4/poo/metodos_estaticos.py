class Persona(object):
    @staticmethod
    def imprimir(parametro1):
        print(parametro1)


objeto = Persona()
objeto.imprimir("valor del parámetro 1")
Persona.imprimir("valor del parámetro 1")

input()
