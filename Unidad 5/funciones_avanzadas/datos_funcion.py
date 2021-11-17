def misuma(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + misuma(L[1:])

print(misuma([1, 2, 3, 4, 5]))
print('',end='\n################\n' )
print(misuma.__name__)  #Obtengo el nombre
print('',end='\n################\n' )
print(dir(misuma))      #Obtengo sus atributos
print('',end='\n################\n' )
print(misuma.__code__)      #Datos de la función
print('',end='\n################\n' )
print(dir(misuma.__code__))      #Datos de la función
print('',end='\n################\n' )
print(misuma.__code__.co_varnames)  #Nombre de variables utilizadas
print('',end='\n################\n' )
print(misuma.__code__.co_argcount)  #Cantidad de argumentos
input()