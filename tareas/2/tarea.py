#
# Copyright (c) 2015 by Julio Seña. All Rights Reserved.
#

'''
Crear un programa en Python que resuelva el siguiente problema de física:
Una ambulancia se mueve con una velocidad de 120 km/h y necesita recorrer un
tramo recto de 60km. Calcular el tiempo necesario, en segundos, para que la
ambulancia llegue a su destino. La fórmula a utilizar es:
velocidad = distancia/tiempo.
'''

# Definicion de constantes
velocidad = 120
distancia = 60

# Se calcula el tiempo empleado en horas
tiempoEnHoras = distancia/velocidad

# Se realiza la conversion de horas a segundos (1 hora = 3600 segundos)
tiempoEnSegundos = tiempoEnHoras * 3600

# Impresion del tiempo en segundos empleado por la ambulacia
print('El tiempo necesario en segundo es de '+str(int(tiempoEnSegundos))+'s.')
