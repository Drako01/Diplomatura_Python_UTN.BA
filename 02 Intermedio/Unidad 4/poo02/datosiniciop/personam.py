class Persona:
    def __init__(self, nombre, edad, sueldo=0, trabajo=None):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.trabajo = trabajo


if __name__ == "__main__":
    Juan = Persona("Juan Garcia", 42, 30000, "software")
    Susana = Persona("Susana Gomez", 45, 40000, "hardware")
    print(Juan.nombre, Susana.sueldo)
    print(Juan.nombre.split()[-1])
    Susana.sueldo *= 1.10
    print(Susana.sueldo)