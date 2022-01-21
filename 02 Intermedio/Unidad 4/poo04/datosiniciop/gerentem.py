from personam import Persona


class Gerente(Persona):
    def dar_aumento(self, porcentaje, premio=0.1):
        self.sueldo *= 1.0 + porcentaje + premio


if __name__ == "__main__":

    Tom = Gerente("Tom Perez", 42, 50000, "software")
    print(Tom.nombre)
    Tom.dar_aumento(0.10, 0.40)
    print(Tom.sueldo)