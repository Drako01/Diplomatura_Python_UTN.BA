def contador_yield1(max):
    n=0
    print("---------")
    while n < max:
        yield n
        print("2----------")
        n+=1

# Retorna el objeto (generador) que guarda el estado de la función. 
d = contador_yield1(3)
print(d)
print('',end='\n####### Ejecuta de inicio de función hasta yield #######\n' )
print(next(d))
print('',end='\n###### Ejecuta de yield a yield #########\n' )
print(next(d))
print('',end='\n################\n' )
print(next(d))
