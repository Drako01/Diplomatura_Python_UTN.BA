import sys
try:
    lista1 = [1,2, 3]
    print(lista1[7]) 
except IndexError as e:

    print(e)
    excepcion = IndexError("hola")
    raise excepcion