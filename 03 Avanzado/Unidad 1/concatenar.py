mistr = 'Pera'
mibyte2 = B'Manzana'
try:
    print(mibyte2 + mistr)
except:
    print('No puedo concatenar un objeto de tipo str con uno de tipo bytes')