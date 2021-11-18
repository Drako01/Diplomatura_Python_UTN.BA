
num = int(input("Ingrese un numero entero: "))
 
if num > 0:
    fact = 1
    x = num
    for i in range(x):
        fact *= x
        x -= 1
    print("El Factorial de ", num, " es: ", fact, ".")   
else:    
    num <= 0
    print("No es posible calcular el Factorial de un Numero menor a 1")