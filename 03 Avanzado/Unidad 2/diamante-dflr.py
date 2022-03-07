class D:
    atributo = 3


class B(D):
    pass


class E:
    atributo = 2


class C:
    atributo = 1


class A(B, C):
    pass


instancia = A()
print(instancia.atributo)
print(A.__mro__)
print(type(A))