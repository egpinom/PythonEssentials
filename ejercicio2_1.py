# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 09:24:54 2022

@author: Gerardo Pino
"""

Datos_2021 = (1, 2, 3, 4, 5, 6, 7,100,91,110,900,21,33,32, 2, 4,8,10,13,13,16,15,1302)
print(f"Tupla inicial:\n{Datos_2021}\n")
pares=[]
impares=[]
atipicos=[]
j=0
for i in Datos_2021:
    if Datos_2021[j]%2==0:
        pares.append(Datos_2021[j])
    else:
        impares.append(Datos_2021[j])
    if Datos_2021[j]>100:
        atipicos.append(Datos_2021[j])
    j+=1
print(f"Los números pares son: {pares}")
print(f"Los números impares son: {impares}")
print(f"Los números atípicos (mayores a 100) son: {atipicos}")