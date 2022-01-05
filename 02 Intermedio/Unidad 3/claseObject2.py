class Auto:
    color = "azul"

# Instanciamos e imprimimos el objeto de la clase Auto
objeto = Auto()
print(objeto.color)

# Imprimimos los métodos de la clase Auto
print(dir(Auto))

# Vemos cual es su clase padre
print(Auto.__class__.__base__)

# Vemos si es un objeto de alguna clase
print(Auto.__class__)
input()
