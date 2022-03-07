import os
archivo1 = os.path.dirname(os.path.abspath(__file__))+"\\archivo1.txt" 

open(archivo1, 'w').write('Escribo algo de texto\n')         
print(open(archivo1, 'r').read())                 
print(open(archivo1, 'rb').read())              

print('----------------------------')
archivo2 = os.path.dirname(os.path.abspath(__file__))+"\\archivo2.txt" 

open(archivo2, 'wb').write(b'Escribo algo de texto\n')         
print(open(archivo2, 'r').read())                 
print(open(archivo2, 'rb').read()) 