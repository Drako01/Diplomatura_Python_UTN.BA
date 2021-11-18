a = 5


def funcion():
    global a
    a = 10  # redefino "a"
    print(a)  # esta es global


funcion()
print(a)


+eval(input())
