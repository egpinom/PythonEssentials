# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 09:55:19 2022

@author: Gerardo Pino
"""

print("Empezando a trabajar con Python")
"""Se usan caracteres de escape para mostrar las comillas dobles"""
print("Realizado por: \"Gerardo Pino\"")
print("Consultando los tipos de valores:")
print("El tipo de dato de 875 es:")
"""Se imprime el valor devuelto por type()"""
print(type(875))
print("El tipo de dato de 4.89 es:")
"""Se imprime el valor devuelto por type()"""
print(type(4.89))
print("El tipo de dato del texto: Now is better than never. es:")
"""Se imprime el valor devuelto por type()"""
print(type("Now is better than never"))
print("El tipo de dato de 1.32 es:")
"""Se imprime el valor devuelto por type()"""
print(type(1.32))
print("¿El valor 5 + 8j corresponde a un valor entero?")
"""Se realiza un casteo a string del valor devuelto por type()"""
"""y se lo compara con el valor que preguntamos, en este caso int"""
if str(type(5+8j)) == "<class 'int'>":
    print("Verdadero")
else:
    print("Falso")
print("¿El valor 8.2 corresponde a un valor entero?")
"""Se realiza un casteo a string del valor devuelto por type()"""
"""y se lo compara con el valor que preguntamos, en este caso int"""
if str(type(8.2)) == "<class 'int'>":
    print("Verdadero")
else:
    print("Falso")
print("¿El texto: Readability counts. corresponde a un string?")
"""Se realiza un casteo a string del valor devuelto por type()"""
"""y se lo compara con el valor que preguntamos, en este caso str"""
if str(type("Readability counts")) == "<class 'str'>":
    print("Verdadero")
else:
    print("Falso")