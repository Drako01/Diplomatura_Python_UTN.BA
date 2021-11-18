tupla1 = 1, 2, 3, 4, 5, 3
print(type(tupla1))
tupla2 = (1, 2, 3, 4, 5, 3)
print(type(tupla2))
tupla3 = tupla1, tupla2
print(type(tupla3))
print(tupla3)

tupla4 = tupla3 + (6, 7)
print(tupla4)
# ######################################
# Determinar un elemento
# ######################################
print(tupla4[0])
# ######################################
# Posición de un elemento
# ######################################
print(tupla4.index(6))
# ######################################
# n° de veces que aparece un elemento
# ######################################
print(tupla4.count(7))
