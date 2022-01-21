from personap.personam import Persona


class Gerente(Persona):
    def dar_aumento(self, porcentaje, premio=0.1):
        self.sueldo *= 1.0 + porcentaje + premio
