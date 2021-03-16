#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 08:57:10 2021

@author: armandonunezbautista
"""
"""
cont1, cont2, cont3, cont4, cont5, cont6 = 0, 0, 0, 0, 0, 0
for x in range(10): # Cambiar a 100
    while True:
        tiro = int(input("Tiro: "))
        if (tiro>0 and tiro<7) :
            break #sale del ciclo
        else:
            print("Número inválido")
    if tiro == 1:
        cont1 = cont1 + 1
    elif tiro == 2:
        cont2 = cont2 +1
    elif tiro == 3:
        cont3 = cont3 +1
    elif tiro == 4:
        cont4 = cont4 +1
    elif tiro == 5:
        cont5 = cont5 +1
    elif tiro == 6:
        cont6 = cont6 +1

print("El 1 salió", cont1, "veces")
print("El 2 salió", cont2, "veces")
print("El 3 salió", cont3, "veces")
print("El 4 salió", cont4, "veces")
print("El 5 salió", cont5, "veces")
print("El 6 salió", cont6, "veces")
"""

def Dominio(lista):
    lista_corr = []
    for x in lista:
        correo = x + "@up.edu.mx"
        lista_corr.append(correo)
    return lista_corr

lista = []
for n in range(3):
    ids = int(input("ID: "))
    ids = str(ids) # Convierto a str para que se pueda sumar\n",
    lista.append(ids)
    
print(Dominio(lista))
