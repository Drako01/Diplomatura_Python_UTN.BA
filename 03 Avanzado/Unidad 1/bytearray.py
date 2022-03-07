mi_string = "Compré una Manzana"
mi_bytearray = bytearray(mi_string, 'latin1')
print(mi_bytearray)
print(mi_bytearray[5])
mi_bytearray[5] = 225
print(mi_bytearray)
print(mi_bytearray.decode('latin1'))