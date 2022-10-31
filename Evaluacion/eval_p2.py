# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 10:17:02 2022

@author: Gerardo Pino
"""

import ejer1_1 as ej1
import ejer1_2 as ej2
import ejer2_1 as ej3
import ejer2_2 as ej4
import ejer3 as ej5

flag=0
while flag!=6:
    print("\nPrograma de Evaluación del Curso Python Essentials")
    print("Opcion 1: Ejercicio 1-1")
    print("Opcion 2: Ejercicio 1-2")
    print("Opcion 3: Ejercicio 2-1")
    print("Opcion 4: Ejercicio 2-2")
    print("Opcion 5: Ejercicio 3")
    print("Opcion 6: Salir.")
    try:
        flag=int(input("Ingrese la opción: "))
        if flag==1:
            ej1.ejer1()
        elif flag==2:
            ej2.ejer2()
        elif flag==3:
           ej3.ejer3()
        elif flag==4:
           ej4.ejer4()
        elif flag==5:
           ej5.ejer5()
        elif flag==6:
            print("Adiós")
        else:
            print("Opción fuera del rango indicado.")
    except:
        print("Error al ingresar el valor del menú.")    
