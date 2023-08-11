# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:19:40 2023

@author: PIPE
"""
Dinamix=18800
tres_D=15500
dos_D=11300

def tipo_sala(sala:str):
    if sala==str(Dinamix):
        return(str(Dinamix))
    if sala==str(tres_D):
        return(str(tres_D))
    if tipo== str(dos_D):
        return(str(dos_D))

def cantidad_boletas(m:int, tipo_sala):
    if tipo_sala==str(Dinamix):
        return(m*Dinamix)
    if tipo_sala==str(tres_D):
        return(m*tres_D)
    if tipo_sala == str(dos_D):
        return(m*dos_D)
    
def hora_pico(hora:bool, cantidad_boletas, tipo_sala):
    
    if(hora==1): 
        
    
        if sala==str(Dinamix):
            return(Dinamix*(1-0.01))
        if sala==str(tres_D):
            return(tres_D*(1-0.01))
        if tipo== str(dos_D):
            return(dos_D*(1-0.01))
        if m>=3:
            if sala==str(Dinamix):
                return(Dinamix*(1-0.01)-500)
            if sala==str(tres_D):
                return(tres_D*(1-0.01)-500)
            if tipo== str(dos_D):
                return(dos_D*(1-0.01)-500)
        
def pago_tarjeta_cinema(pago:bool):
    if pago == 1: 
        Dinamix=Dinamix*(1-0.05)
        tres_D=tres_D*(1-0.05)
        dos_D=dos_D*(1-0.05)
    else: 
        Dinamix=18800
        tres_D=15500
        dos_D=11300
    
def reserva():

def calcular_costo_boletas():

    
