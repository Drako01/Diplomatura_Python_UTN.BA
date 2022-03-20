def decorator(cls):
    class Envoltura:
        def __init__(self, *args):
            self.instanciaDeClaseOriginal = cls(
                *args
            )  # genero instancia de la clase original

        def __getattr__(self, nombre):
            print(self, "  -----  Instancia de Envoltura")
            print(self.instanciaDeClaseOriginal, "  -----  Instancia de Auto.")
            print("Nombre de atributos de clase Auto: ", nombre)
            return getattr(
                self.instanciaDeClaseOriginal, nombre
            )  # Retorna el valor del atributo de la clase C llamado

    return Envoltura


@decorator
class Auto:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca


x = Auto("Rojo", "Renault")
print(x.color)
print(x.marca)