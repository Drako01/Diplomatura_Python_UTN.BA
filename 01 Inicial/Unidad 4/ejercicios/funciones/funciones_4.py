a = 5
b = 6


def nopisa():
    a = 10
    print("La variable 'a' dentro de la función tiene por valor", a)
    print("'b' es global, por lo que puedo impirmirla acá", b)


nopisa()
print("La variable 'a' fuera de la función tiene por valor", a)
print("", end="\n################\n")
# +eval(input())
