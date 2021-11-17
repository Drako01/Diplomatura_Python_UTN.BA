def f(a, *args):
    print("Tupla de valores: ", args)
    print("Lista de valores: ", *args)
    for arg in args:
        print("Elemento de la tupla: ", arg)


f(0, 1, 2, "Manzana")
