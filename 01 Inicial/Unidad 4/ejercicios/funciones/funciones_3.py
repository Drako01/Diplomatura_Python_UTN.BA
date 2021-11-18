a = 5  # a es global


def sumar_cinco(b):
    c = a + b  # b y c son locales a la función
    return c


print(sumar_cinco(5))
# +eval(input())
