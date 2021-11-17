# ##############################################
# Recursión ####
# ##############################################
def miSuma(L):
	return 0 if not L else L[0] + miSuma(L[1:]) # Uso de expresión ternaria

print(miSuma([1, 2, 3, 4, 5]))	
print('',end='\n################\n' )	
	
L = [1, 2, 3, 4, 5]
suma = 0
while L:
	suma += L[0]
	L=L[1:]
print(suma)


input()