
# def obtener_vocales(frase):
#     vocales = 'aeiouAEIOU'

#     return set([c for c in frase if c in vocales])


# texto = str(input("Ingrese una Palabra:"))

# import re
# sentence = texto

# print('occurrence of letter a:', len(re.findall(texto, sentence)))
# print("Las Vocales son:",obtener_vocales(texto))
# print("Hay", len(obtener_vocales(texto)),"Vocal/es")

cadena = str(input("Ingrese una Palabra:"))
def contar_vocales(cadena):
	contador = 0
	for letra in cadena:
		if letra.lower() in "aeiou":
			contador += 1
	return contador


cantidad = contar_vocales(cadena)
print(f"En la cadena '{cadena}' hay {cantidad} vocales")