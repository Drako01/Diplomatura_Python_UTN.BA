class B(Exception):
    color = "ROJO"

class C(B):
    color = "VERDE"

class D(C):
    color = "AZUL"


 
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
        print(D.color)
    except C:
        print("C")
        print(C.color)
    except B:
        print("B")
        print(B.color)
 
