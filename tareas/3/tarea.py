#
# Copyright (c) 2015 by Julio Seña. All Rights Reserved.
#

'''
Escriba un programa en Python donde el usuario introduce un numero n y
el programa imprime los primeros n numeros triangulares,
junto con su indice. Los numeros triangulares se originan
de los numeros naturales desde 1 hasta n. Ejempo.
'''

# Se valida que sea un numero
try:
    numero = int(input("Por favor escriba un numero: "))
except ValueError:
    print("Por favor debe ser un numero Natural")
    numero = 0

index = 0
result = 0

# Se evalua que sea un numero natural
if numero < 0:
    print("El numero no es natural")
else:
    while (index <= numero):
        result += index
        index += 1

# Se realiza la impresion por pantalla
    print(str(numero) + " - " + str(result))
