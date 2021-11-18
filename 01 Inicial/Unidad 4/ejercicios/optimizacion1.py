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


def recorrer_lista(item, nivel):  # Agrego segundo parámetro
    for x in item:
        if isinstance(x, list):
            recorrer_lista(x, nivel + 1)
        else:
            for y in range(nivel):
                print((""))
            print(x)


recorrer_lista(lista, 0)
