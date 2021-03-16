#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 13:05:02 2021

@author: armandonunezbautista
"""
##################################################################################################################

"""
def dias(mes):   
    #if (mes.lower() in("enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre")):
    if (mes.lower() == ("enero" or "marzo" or "mayo" or "julio" or "agosto" or "octubre" or "diciembre")):      
        return "31"
    elif (mes.lower() == "febrero"):
        return "29"
    else:
        return "30"
    
    
mes = input("Mes: ")

print(dias(mes))

"""
##################################################################################################################
"""
def dias_mes(mes):
    if mes == "enero" or mes == "marzo" or mes == "mayo" or mes == "julio" or mes == "agosto" or mes == "octubre" or mes == "diciembre":
        return "31"
    elif mes == "febrero":
        return "29"
    else:
        return "30"
    
    
while True:
    mes = input("Mes: ")
    mes = mes.lower()
    if (mes == "enero" or mes == "febrero" or mes == "marzo" or mes == "abril" or mes == "mayo" or mes == "junio" or mes == "julio" or mes == "agosto" or mes == "septiembre" or mes == "octubre" or mes == "noviembre" or mes == "diciembre"):
        break
    else:
        print("No es un mes")

print("El mes de", mes,"tien", dias_mes(mes), "dias")
"""

##################################################################################################################
"""
# Variables iniciadoras
sum_ventas, mayor, menor, ventaM, ventam = 0, -999999, 999999, 0, 0

num = int(input("Número de vendedores: "))
for vendedor in range(num):
    ventas = float(input("Ventas del vendedor"))
    sum_ventas = sum_ventas + ventas
    if (ventas > mayor):
        mayor = ventas
        ventaM = vendedor
    if (ventas < menor):
        menor = ventas
        ventam = vendedor
prom_ventas = sum_ventas / num
        
print("- Promedio de ventas:", prom_ventas)
print("- Total de ventas", sum_ventas)
print("- La mayor venta fue de", mayor, "por el vendedor", (ventaM+1))
print("- La menor venta fue de", menor, "por el vendedor", (ventam+1))
"""
##################################################################################################################
"""
# Lista 

nombre = input("Nombre: ")
apellido = input("Apellido Paterno: ")
edad = int(input("Edad: "))
nacion = input("Nacionalidad: ")
telefono = int(input("Teléfono: "))

datos_l = [nombre, apellido, edad, nacion, telefono]

print("\n")
print(datos_l[0], datos_l[1], "tiene", datos_l[2], "años, su nacionalid es", datos_l[3], " y su teléfono es", datos_l[4])

"""
"""
# Tupla

nombre = input("Nombre: ")
apellido = input("Apellido Paterno: ")
edad = int(input("Edad: "))
nacion = input("Nacionalidad: ")
telefono = int(input("Teléfono: "))

datos_t = (nombre, apellido, edad, nacion, telefono)

print("\n")
print(datos_t[0], datos_t[1], "tiene", datos_t[2], "años, su nacionalidad es", datos_t[3], "y su teléfono es", datos_t[4])
"""
"""
# Diccionario 

nombre = input("Nombre: ")
apellido = input("Apellido Paterno: ")
edad = int(input("Edad: "))
nacion = input("Nacionalidad: ")
telefono = int(input("Teléfono: "))

datos_d = {"Nombre":nombre, "ApellidoP":apellido, "Edad":edad, "Nacionalidad":nacion, "Teléfono":telefono}
print("\n")
print(datos_d["Nombre"], datos_d["ApellidoP"], "tiene", datos_d["Edad"], "años, su nacionalidad es", datos_d["Nacionalidad"], "y su teléfono es", datos_d["Teléfono"])
"""

##################################################################################################################
"""
# Lista

datosL_frutas = ["plátano", "manzana", "uva", "naranja"]
frutaL= input("¿Qué fruta quieres?: ")
frutaL = frutaL.lower()
kgL = float(input("¿Cuántos kilos?: "))

if frutaL in datosL_frutas[0]:
    conversionL = 23.9*kgL
    print(kgL, "kilos de", frutaL, "cuestan $", conversionL)

elif frutaL in datosL_frutas[1]:
    conversionL = 46.9*kgL
    print(kgL, "kilos de", frutaL, "cuestan $", conversionL)

elif frutaL in datosL_frutas[2]:
    conversionL = 56*kgL
    print(kgL, "kilos de", frutaL, "cuestan $", conversionL)

elif frutaL in datosL_frutas[3]:
    conversionL = 16.9*kgL
    print(kgL, "kilos de", frutaL, "cuestan $", conversionL)

else :
    print("\n")
    print("Lo siento, la fruta", frutaL, "no está disponible.")
"""

# Tupla 

datosT_frutas = ("plátano", "manzana", "uva", "naranja")
frutaT= input("¿Qué fruta quieres?: ")
frutaT = frutaT.lower()
kgT = float(input("¿Cuántos kilos?: "))

if frutaT in datosT_frutas[0]:
    conversionT = 23.9*kgT
    print(kgT, "kilos de", frutaT, "cuestan $", conversionT)

elif frutaT in datosT_frutas[1]:
    conversionT = 46.9*kgT
    print(kgT, "kilos de", frutaT, "cuestan $", conversionT)

elif frutaT in datosT_frutas[2]:
    conversionT = 56*kgT
    print(kgT, "kilos de", frutaT, "cuestan $", conversionT)

elif frutaT in datosT_frutas[3]:
    conversionT = 16.9*kgT
    print(kgT, "kilos de", frutaT, "cuestan $", conversionT)

else :
    print("\n")
    print("Lo siento, la fruta", frutaT, "no está disponible.")


"""
# Diccionario

datos_frutas = {"plátano":23.9, "manzana":46.9, "uva":56, "naranja":16.9}
fruta = input("¿Qué fruta quieres?: ")
fruta = fruta.lower()
kg = float(input("¿Cuántos kilos?: "))
if fruta in datos_frutas:
    conversion = datos_frutas[fruta]*kg
    print("\n")
    print(kg, "kilos de", fruta, "cuestan $", conversion)
else:
    print("\n")
    print("Lo siento, la fruta", fruta, "no está disponible.")
    
"""


 
    