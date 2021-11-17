# ##############################################
# Recursión ####
# ##############################################


def miSuma(L):
    return 0 if not L else L[0] + miSuma(L[1:])  # Uso de expresión ternaria


def miSuma1(L):
    return L[0] if len(L) == 1 else L[0] + miSuma1(L[1:])


def miSuma2(L):
    first, *rest = L
    return first if not rest else first + miSuma2(rest)

print(miSuma([1, 2, 3, 4, 5]))
print('',end='\n################\n' )
print(miSuma1([1, 2, 3, 4, 5]))
print('',end='\n################\n' )
print(miSuma2([1, 2, 3, 4, 5]))

input()