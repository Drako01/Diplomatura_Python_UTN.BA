def funcion(a, *pargs, **kwargs):
    print(a, pargs,kwargs)
    print("-----------")
    print(a)
    print("-----------")
    print(pargs)
    print("-----------")
    if kwargs is not None:
        for clave, valor in kwargs.items():
            print( "%s == %s" %(clave, valor))

funcion(1, 2, 3, nombre="Juan", edad=1, sexo="Masculino")




#def f(a, *pargs, **kargs): print(a, pargs, kargs)
#f(1, 2, 3, x=1, y=2)

