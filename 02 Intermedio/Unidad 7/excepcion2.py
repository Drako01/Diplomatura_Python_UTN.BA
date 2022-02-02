def sumar(a, b):
    c = a + b
    return c


print(sumar(3, 4))

try:
    print(sumar(3, "Manzana"))
except:
    print("Ha surgido un error")

print(sumar(2, 3))
