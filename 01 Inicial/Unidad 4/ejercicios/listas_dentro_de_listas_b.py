lista = [
    "elemento1n1",
    "elemento2n1",
    "elemento3n1",
    [
        "elemento1n2",
        "elemento2n2",
        "elemento3n2",
        ["elemento1n3", "elemento2n3", "elemento3n3"],
    ],
]
# imprimimos la lista
print(lista)
print("", end="\n################\n")
# imprimimos elementos de primer nivel
for a in lista:
    print(a)
print("", end="\n################\n")
# imprimimos elementos de primer y segundo nivel
# con el if veo si el elemento de lista no es una lista
# si es una lista recorro la lista y sino paso al siguiente elemento
for a in lista:
    if isinstance(a, list):
        for b in a:
            print(b)
    else:
        print(a)
print("", end="\n################\n")
# imprimimos elementos de primer y segundo y tercer nivel
# con el if veo si el elemento de lista no es una lista
# si es una lista recorro la lista y sino paso al siguiente elemento
for a in lista:
    if isinstance(a, list):
        for b in a:
            if isinstance(b, list):
                for c in b:
                    print(c)
            else:
                print(b)
    else:
        print(a)
