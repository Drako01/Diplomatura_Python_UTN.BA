import random

numero = random.randint(-5, 5)

try:
    if numero < 0:
        raise TypeError("No se puede calcular la raiz")
    print("numero %.2f y su raíz cuadrada %.2f" % (numero, numero ** 0.5))
except (TypeError) as mensaje:
    print("Ocurrió una excepción identificada.", mensaje)
