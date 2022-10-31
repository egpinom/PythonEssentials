# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:45:49 2022

@author: Gerardo Pino
"""

def evaluacion(dicc_eval):
    """La función evaluará los máximos y mínimos cuando los valores del"""
    """diccionario sean valores numéricos, en caso de listas o tuplas no se"""
    """ordenará el diccionario."""
    while True:
        err=False
        err1=False
        err2=False
        while True:
            try:
                max_1=int(input("\nDigite el número de valores altos que desea mostrar: "))
                break
            except:
                print("Error al ingresar el valor de máximos, vuelva a ingresarlo.")
        while True:
            try:
                min_1=int(input("Digite el número de valores bajos que desea mostrar: "))
                break
            except:
                print("Error al ingresar el valor de mínimos, vuelva a ingresarlo.")
        tam=len(dicc_eval)
        if max_1>tam:
            print("Número de Máximos ingresado supera el tamaño del diccionario.")
            err1=True
        if min_1>tam:
            print("Número de Mínimos ingresado supera el tamaño del diccionario.")
            err2=True
        if max_1<0 or min_1<0:
            print("Número ingresado es menor a cero.")
            err2=True
        err=err1 or err2
        if err:
            print("\nError al ingresar los valores de máximos y mínimos, vuelva a ingresarlos.")    
        else:
            dicc_min=dict(sorted(dicc_eval.items(), key=lambda item:item[1]))
            dicc_max=dict(sorted(dicc_eval.items(), key=lambda item:item[1], reverse=True))
            lst2_max=[]
            lst2_min=[]
            tpl2_max=()
            tpl2_min=()
            j=0
            k=0
            for i in dicc_max:
                if j<max_1:
                    lst2_max.append(dicc_max[i])
                    j+=1
                else:
                    break
            for i in dicc_min:
                if k<min_1:
                    lst2_min.append(dicc_min[i])
                    k+=1
                else:
                    break
            tpl2_max=tuple(lst2_max)
            tpl2_min=tuple(lst2_min)
                
            print(f"Valores máximos calculados en formato LISTA: {lst2_max}")
            print(f"Valores máximos calculados en formato TUPLA: {tpl2_max}")
            print(f"Valores mínimos calculados en formato LISTA: {lst2_min}")
            print(f"Valores mínimos calculados en formato TUPLA: {tpl2_min}")
            break
    return    

while True:
    print("\nPrograma de máximos y mínimos de un diccinario.")
    print("1) Demostración del cálculo de valores altos y bajos en diccionarios.")
    print("2) Salir.")
    try:
        flag1=int(input("Ingrese la opción: "))
        if flag1==1:
            while True:
                print("\nEscoja un diccionario para su análisis:")
                print("1) {Raul:34,Paula:19,Jorge:43,Richard:10,Diana:3,Isabel:76,Gustavo:12,Diego:37}")
                print("2) {tplA:(4,-12,56,-34,98,102),tplB:(9,0,1,10,-3,14),tlpC:(87,12,56,987,-61)}")
                print("3) {val1:-12.5,val2:12.5,val3:83,val4:2.1,val5:23,val6:100,val7:13.4,val8:92}")
                print("4) {lst1:[4,6,-12,56,-9,5.7,33,100],lst2:[9,0,81,-2,-56,],lst3:[12,31,87,1,0,4,-11]}")
                try:
                    flag2=int(input("Seleccione el diccionario: "))
                    if flag2==1:
                        dicc1={"Raul":34,"Paula":19,"Jorge":43,"Richard":10,"Diana":3,"Isabel":76,"Gustavo":12,"Diego":37}
                        evaluacion(dicc1)
                        break
                    elif flag2==2:
                        dicc2={"tplA":(4,-12,56,-34,98,102),"tplB":(9,0,1,10,-3,14),"tlpC":(87,12,56,987,-61)}
                        evaluacion(dicc2)
                        break
                    elif flag2==3:
                        dicc3={"val1":-12.5,"val2":12.5,"val3":83,"val4":2.1,"val5":23,"val6":100,"val7":13.4,"val8":92}
                        evaluacion(dicc3)
                        break
                    elif flag2==4:
                        dicc4={"lst1":[4,6,-12,56,-9,5.7,33,100],"lst2":[9,0,81,-2,-56,],"lst3":[12,31,87,1,0,4,-11]}
                        evaluacion(dicc4)
                        break
                    else:
                        print("\nOpción de diccionario incorrecta, vuelva a ingresarla.")
                except:
                    print("\nError al ingresar el diccionario, vuelva a intentarlo.")
        elif flag1==2:
            print("\nAdiós.")
            break
        else:
            print("\nOpción fuera del rango, vuelva a ingresarla.")
    except:
        print("\nError al ingresar la opción, vuelva a intentarlo.")