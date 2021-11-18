numero = int(input("Escriba un Número:"));

def nroAscendentes(i):
    for x in range(i+1):
        yield str(x)
        
def nroDescendentes(i):
    for x in range(i, -1, -1):
        yield str(x)


print ("Los Números ordenados de forma ascendentes son: ",", ". join(nroAscendentes(numero)))
print ("Los Números ordenados de forma descendentes son: ",", ". join(nroDescendentes(numero)))

