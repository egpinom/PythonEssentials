# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:41:26 2022

@author: Gerardo Pino
"""

def ejer2():
    print("\nPrograma que identifica el tipo de dato de un valor ingresado por el usuario, se realizarán cinco interacciones: ")
    i=0
    while i<5:
        if i+1==1:
            str1="Primera "
        elif i+1==2:
            str1="Segunda "
        elif i+1==3:
            str1="Tercera "
        elif i+1==4:
            str1="Cuarta "
        else:
            str1="Quinta "
        str1+="Interacción, ingrese un valor cualquiera: "
        vlr1=input(str1)    
        """Si sólo se hace type() del valor ingresado por input(), el resultado"""
        """será siempre un string (str). Se usan excepciones y casteos para"""
        """determinar el tipo de dato."""
        try:
            res=int(vlr1)
            tipo="Entero"
        except ValueError: 
            try:
                res=float(vlr1)
                tipo="Flotante"
            except ValueError:
                try:
                    res=complex(vlr1)
                    tipo="Complejo"
                except ValueError:
                    try:
                        res=complex(vlr1)
                        tipo="Complejo"
                    except ValueError:
                        try:
                            res=str(vlr1)
                            tipo="Cadena"
                            if res=="True":
                                tipo="Booleano"
                            elif res=="False":
                                tipo="Booleano"
                        except:
                            tipo="Desconocido"
        print(f"Este tipo de dato en Python es: {tipo}")
        """Esta sentencia haría que se muestre únicamente <class 'str'>, sin"""
        """importar lo que ingresemos por teclado."""
        """print(f"Este tipo de dato en Python es: {type(vlr1)}")"""
        i+=1
    print("\nFin del programa")
    return