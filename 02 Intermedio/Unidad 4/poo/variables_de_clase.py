class Persona(object):
    empresa = "Empresa1"

    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

        print(self.nombre)

    def datos(self, salario):
        print(
            "Nombre de la persona: "
            + self.nombre
            + "\n"
            + "Salario en $: "
            + str(salario)
        )


objeto = Persona("Juan", 39, "masculino")

objeto.datos(100)
print(Persona.empresa)
print(objeto.empresa)
print(objeto.edad)
input()
