from personap.personam import Persona


class Gerente(Persona):
    def __init__(self, nombre, edad, sueldo):
        Persona.__init__(self, nombre, edad, sueldo, "Gerente")

    def dar_aumento(self, porcentaje, premio=0.1):
        Persona.dar_aumento(self, porcentaje + premio)
