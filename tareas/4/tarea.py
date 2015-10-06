'''TAREA
-----
Fecha de Revisión: 12/10/2015
-----

Instrucciones:
--------------
1. Dado un intervalo de tiempo en minutos, calcular los días, horas y minutos
correspondientes.

'''

minutos = int(input("Por favor escriba el tiempo en minutos: "))

dias = int(minutos / 1440)
minutos = minutos % 1440
horas = int(minutos / 60)
minutos = minutos % 60

print('D: ' + str(dias) + ', H: ' + str(horas) + ', M: ' + str(minutos))
