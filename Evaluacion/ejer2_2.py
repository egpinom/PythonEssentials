# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:47:33 2022

@author: Gerardo Pino
"""

def validate(lst1,pwd_lst):
    j=0
    validate=0
    for i in pwd_lst:
          if pwd_lst[j] in lst1:
              validate=1
              return validate
          j+=1
    return validate

def ejer4():
    print("\nPrograma Validador de Contraseña. Al crear su contraseña debe tener en cuenta los siguientes criterios:\n")
    print("* Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j.")
    print("* Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T.")
    print("* Debe contener al menos un número entre 0 y 9.")
    print("* Debe contener un símbolo especial entre: $,%,*,@.")
    print("* Tamaño mínimo de 5 caracteres y máximo de 15.")
    while True:
        password=input("Introduzca su contraseña: ")
        pwd_lst=list(password)
        if len(password)<5:
            print("Su contraseña debe tener mínimo 5 caracteres")
        elif len(password)>15:
            print("Su contraseña debe tener máximo 15 caracteres")
        else:
            spc_char=validate(["$","%","*","@"],pwd_lst)
            num_char=validate(["0","1","2","3","4","5","6","7","8","9"],pwd_lst)
            min_char=validate(["a","b","c","d","e","f","g","h","i","j"],pwd_lst)
            may_char=validate(["K","L","M","N","O","P","Q","R","S","T"],pwd_lst)
            if spc_char and num_char and may_char and min_char:
                print("\nSu contraseña ha sido validada de forma correcta.")
                break
            else:
                print("\nSu contraseña no es válida, por favor revise:")
                if not spc_char:
                    print("* No contiene los caracteres especiales indicados.")
                if not num_char:
                    print("* No contiene números.")
                if not may_char:
                    print("* No tiene letras mayúsculas en el rango indicado.")
                if not min_char:
                    print("* No tiene letras minúsculas en el rango indicado.")
                print()
    return