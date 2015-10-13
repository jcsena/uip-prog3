#
# Copyright (c) 2015 by Julio Seña. All Rights Reserved.
#
'''

dado un itervalo de tiempo en segundos, calcular los segundos
restantes que corresponden para convertirse exactamente en minutos
este programa debe funcionar debe funcionar para 5 oportunidades

'''

# Lista de segundos capturados
rep = []

# Numero de solicitudes que debe realizar
numRep = 5

# Incrementador en el while
i = 0
while i < numRep:
    i += 1

    # Se solicita el numero de segundos por pantalla
    x = input("Escriba en numero de segundos para el  " + str(i) + " caso : ")

    # Se agrega  la lista en numero registrado
    rep.append(float(x))

j = 0
for tiempo in rep:
    j += 1
    restante = tiempo % 60
    paraMin = 60 - restante
    print("Para " + str(j) + " los segundos restantes son: " + str(paraMin))
