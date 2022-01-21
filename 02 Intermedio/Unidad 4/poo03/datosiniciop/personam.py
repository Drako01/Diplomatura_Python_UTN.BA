class Persona:
    def __init__(self, nombre, edad, sueldo=0, trabajo=None):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.trabajo = trabajo

    def apellido(self):
        return self.nombre.split()[-1]

    def dar_aumento(self, porcentaje):
        self.sueldo *= 1.0 + porcentaje


if __name__ == "__main__":
    Juan = Persona("Juan Garcia", 42, 30000, "software")
    Susana = Persona("Susana Gomez", 45, 40000, "hardware")
    print(Juan.nombre, Susana.sueldo)
    print(Juan.apellido())
    Susana.dar_aumento(0.10)
    print(Susana.sueldo)