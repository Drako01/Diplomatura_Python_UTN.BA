__all__ = ["variable_a_compartir1", "funcion_a_compartir1"]

variable_privada1 = "Hola variable privada 1"
variable_a_compartir1 = "Hola variable pública 1"


def funcion_a_compartir1():
    return "Hola función pública 1"


print("i-----------------------")
print(variable_privada1)
print(variable_a_compartir1)
print(funcion_a_compartir1())
print("f-----------------------")
