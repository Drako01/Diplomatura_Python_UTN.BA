import pprint

print("En una sola línea")
"""
En una sola línea
"""
########  con variable  ########
a = "Desde una variable"
print(a)
"""
Desde una variable
"""
########  Desde una secuencia - Opción para multilínea - LISTA ########
seq = [1, 2, 3, 4]
a, b, c, d = seq
print(a, b, c, d)
"""1 2 3 4"""
########  Desde una secuencia - Opción para multilínea - LISTA ########
a, *b = seq
print(a)
print(b)
print(a, b, type(b))
"""
1
[2, 3, 4]
1 [2, 3, 4]
"""
########  Desde una secuencia - Opción para multilínea  - LISTA ########
a, *b, c = seq
print(a, b, c)
"""
1 [2, 3] 4
"""
########  Desde una secuencia - Opción para multilínea STRING ########
a, *b = "Manzana"
print(a, b, type(b))
"""
s ['p', 'a', 'm']
"""
########  Desde una secuencia - Opción para multilínea ENTEROS ########
a, *b, c = range(4)
print(a, b, c)
"""
0 [1, 2] 3
"""
############## Ejemplo con while y LISTA ##############################
lista = [1, 2, 3, 4]
while lista:
    front, *lista = lista
    print(front, lista)
"""
1 [2, 3, 4]
2 [3, 4]
3 [4]
4 []
"""
#################################

lista2 = [1, 2]
lista2.append(3)
print(lista2)

######################  La asignación en el lugan no la puedo imprimir retorna None
print(lista2.append(4))

######## FORMATEO DE LA SALIDA DE PRINT #######################
x = "hola"
y = 99
z = ["tres", 4]
print(x, y, z, sep="")  # Suprime la coma
print(x, y, z, sep="/ ")  # Indicamos el tipo de separador
print(x, y, z, end="")
print(x, y, z)
# Uso de punto y coma para varios print en línea
print(x, y, z, sep="...", end="!\n")
# Uso de varias declaraciones


################ FORMATO EN MULTILÍNEAS ############################
## http://docs.python.org/library/stdtypes.html#string-formatting-operations ##
text = "%s: %-.4f, %05d" % ("Result", 3.14159, 42)
print(text)

text1 = "%s: %-.4f, %05d" % ("Result", 3.14159, 42)
print(text1)


################### AUMENTAR LA LEGIBILIDAD ############################
juan = {
    "identificacion": {"nombre": "Juan", "apellido": "Garcia"},
    "edad": 24,
    "sueldo": 5000,
    "profesión": "Pintor",
}
susana = {
    "identificacion": {"nombre": "Susana", "apellido": "Gomez"},
    "edad": 25,
    "sueldo": 6000,
    "profesión": "Empleada",
}
db = {}
db["juan"] = juan
db["susana"] = susana
print(db)
print("------------------------------")

pprint.pprint(db)
################### AUMENTAR LA LEGIBILIDAD ############################
A = """
Texto en
muchas líneas
a imprimir
"""
print(A)
pprint.pprint(A)
