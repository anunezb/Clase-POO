# -*- coding: utf-8 -*-
"""
Ejercicios Clase

"""

## 1. Escribe un programa que haga raices cuadradas. Valida que el numero no sea negativo
"""
import math

for x in range(4):
    while True:
        num=int(input("Numero: "))
        if num>0:
            break
        else:
            print("numero invalido")
    raiz=math.sqrt(num)
    print(raiz)
"""

## 2. Leer caracteres hasta que el usuario haya dado cinco asteriscos

for x in range(5):
    while True:
        carcter = input ("Caracter: ")
        if carcter == "*":
            print(carcter)
            break
        else:
            print("No valido")
            