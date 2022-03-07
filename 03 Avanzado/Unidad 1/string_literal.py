fruta1 = b'Manzana'    # 3.X bytes literal crea un objeto de bytes de 8 bits. 
fruta2 = 'Pera'        # 3.X str literal crea un texto Unicode. 
print(type(fruta1))
print(type(fruta2))
print(fruta1.decode('ascii'))
print(type(fruta1.decode('ascii')))
print(fruta2.encode('ascii'))
print(type(fruta2.encode('ascii')))