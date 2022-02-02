def buscar(objeto, clave):
    return objeto[clave]
   
palabra = "Manzana"
print(buscar('manzana', 3))   

try: 
    print(buscar('manzana', 31))
    if buscar('manzana', 31) == False:
        print("ddddddd")
except IndexError:
    print('Ha existido un error')

