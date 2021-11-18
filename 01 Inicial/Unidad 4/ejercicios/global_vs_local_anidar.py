nivel0 = 0


def f1():
    nivel1 = 1

    def f2():
        nivel2 = 2
        print(nivel0, nivel1, nivel2)

    f2()
    print(nivel0, nivel1)


f1()
print(nivel0)
