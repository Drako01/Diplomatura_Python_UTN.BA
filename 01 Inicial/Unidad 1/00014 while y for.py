#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 20:51:45 2021

@author: maromans
"""
"""
Problema 1:
Mostrar la tabla de multiplicar del 5 empleando primero el while y seguidamente de nuevo empleando el for.
"""

print ("usando el while")
x=5
while x<55:
    print (x)
    x=x+5

print(" terminado con while")
print ("usando el for")
for x in range(5,55,5):
    print (x)
print("teminado con for")

"""
Problemas propuestos

Realizar un programa que solicite la carga de valores enteros por teclado y los sume. Finalizar la carga al ingresar el valor -1. Dejar como comentario dentro del código fuente el enunciado del problema.
"""
suma=0
val=0
while val!=-1:
    val=int(input(f"ingrese valores positivos por teclado ingrese -1 para detener y ver el resultado "))
    suma=suma+val
print(f"la suma de los valores ingresados es: {suma}")
"""
Confeccionar un programa que solicite la carga de 10 valores reales por teclado. Mostrar al final su suma. Definir varias líneas de comentarios indicando el nombre del programa, el programador y la fecha de la última modificación. Utilizar el caracter # para los comentarios
"""

#programador mansilla marcelo 18 de octubre de 2021
# ver 1.0
x=0
suma=0
for y in range(0,10,1):#for esta desde 0 a10 con pasos de  1
    x=int(input(f"ingrese un numero asi lo sumamos: "))
    suma=suma+x #aca sumamos a suma el valor ingresado
print(f"la suma de los valores ingresados es {suma}")#los resultados
