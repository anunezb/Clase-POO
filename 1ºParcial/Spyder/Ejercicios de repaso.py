#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
"Ejercicios de repaso "

"""

# Ejercicio 3 

def fun(cadena, num):
    return cadena*num


# Main

cadena = input("Cadena: ")
while True:
    num = int(input("Numero: "))
    if (num>0) :
        break #sale del ciclo
    else:
        print("Caracter invalido") 
print(fun(cadena,num))