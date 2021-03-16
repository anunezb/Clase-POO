#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 16:23:26 2021

@author: armandonunezbautista
"""

"""
# Ejercicio 1 ________________________________________________________________

class Instrumento:
    porc_comision = 10 # Atributo de clase
    def __init__(self, num_tit, p_venta, p_compra): # Atributos de instancia
        self.num_tit = num_tit
        self.p_venta = p_venta
        self.p_compra = p_compra
        # Iniciar variables
        self.__ganancia, self.sub_monto_c, self.com, self.monto_total = 0, 0, 0, 0
        self.sub_monto_v, self.com_v, self.monto_total_v = 0, 0, 0
    def ganancia(self):
        self.__ganancia = self.num_tit*(p_venta-p_compra)
        return self.__ganancia
    def compra(self):
        self.sub_monto_c = self.num_tit*self.p_compra
        self.com = self.sub_monto_c*(Instrumento.porc_comision/100)
        self.monto_total = self.sub_monto_c + self.com 
        return self.monto_total 
    def venta(self):
        self.sub_monto_v = self.num_tit*self.p_venta
        self.com_v = self.sub_monto_v*(Instrumento.porc_comision/100)
        self.monto_total_v = self.sub_monto_v + self.com_v
        return self.monto_total_v


# Main %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

num_tit = int(input("Número de títulos: "))
p_venta = float(input("Precio de venta: "))
while True:
    p_compra = float(input("Precio de compra: "))
    if p_compra < p_venta:
        break #sale del ciclo
    else:
        print("Invalido")

factura = Instrumento(num_tit, p_venta, p_compra)
print("\n- La ganancia fue de: $",factura.ganancia())
print("- El monto de compra fue de: $",factura.compra())
print("- El monto de venta fue de: $",factura.venta())
"""

   
"""
# Ejercicio 2_________________________________________________________________

class Juego:
    def __init__(self, t_comprado, tipo_cliente):
        self.t_comprado = t_comprado
        self.tipo_cliente = tipo_cliente
        # Iniciar variables
        self.t_aire, self.acum_t_aire, self.ex, self.cuota = 0, 0, "", 0
    def monto(self):
        # Actualizar tiempo
        while self.t_comprado > 0:
            self.t_aire = int(input("Tiempo aire de sesión: "))
            self.t_comprado = self.t_comprado - self.t_aire
            self.acum_t_aire = self.acum_t_aire + self.t_aire
        # Monto
        if self.tipo_cliente == "VIP":
            self.ex = input("Extender (si/no): ")
            if self.ex == "si":
                self.cuota = (self.acum_t_aire*18) + 10
                print("Monto a pagar: $", self.cuota)
            else:
                print("\nGame Over")
                self.cuota = self.acum_t_aire*18
                print("Monto a pagar: $", self.cuota)
        elif self.tipo_cliente == "NORMAL":
            print("\nGame Over")
            self.cuota = self.acum_t_aire*20
            print("Monto a pagar: $", self.cuota)
            
        
# Main %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

t_comprado = int(input("Tiempo comprado: "))
tipo_cliente = input("Tipo de cliente (VIP / Normal): ")
tipo_cliente = tipo_cliente.upper()

usuario = Juego(t_comprado, tipo_cliente)

usuario.monto()
"""


class Juego:
    def __init__(self, t_comprado, tipo_cliente):
        self.t_comprado = t_comprado
        self.tipo_cliente = tipo_cliente
        # Iniciar variables
        self.t_aire, self.acum_t_aire, self.ex, self.cuota = 0, 0, "", 0
    def monto(self):
        # Actualizar tiempo
        while self.t_comprado > 0:
            self.t_aire = int(input("Tiempo aire de sesión: "))
            self.t_comprado = self.t_comprado - self.t_aire
            self.acum_t_aire = self.acum_t_aire + self.t_aire
        # Monto
        if self.tipo_cliente == "VIP":
            self.ex = input("Extender (si/no): ")
            if self.ex == "si":
                self.acum_t_aire = self.acum_t_aire + 60
                self.cuota = (self.acum_t_aire*18) + 10
            else:
                print("\nGame Over")
                self.cuota = self.acum_t_aire*18
        elif self.tipo_cliente == "NORMAL":
            print("\nGame Over")
            self.cuota = self.acum_t_aire*20
        return self.cuota
            
        
# Main %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

t_comprado = int(input("Tiempo comprado: "))
tipo_cliente = input("Tipo de cliente (VIP / Normal): ")
tipo_cliente = tipo_cliente.upper()

usuario = Juego(t_comprado, tipo_cliente)

print("Monto a pagar: $", usuario.monto())













