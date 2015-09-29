#
# Copyright (c) 2015 by Julio Seña. All Rights Reserved.
#
'''
El empleador esta celebrando aniversario y ofrecera a sus clientes una serie
de ofertas que se traduciran en incremeno de sus ventas. Las reglas de la
ofertas se basan en un porcentaje de descuento sobre el total de compra, que
estarian variando dependiendo del monto adquirido:

por un monto mayor o igual a $500 -> 30%
por un monto menor de $500 y mayor que 200 -> 20%
por un monto menor de $200 -> y mayor o igual a $100 -> 10%
'''

# Se define la lista de clientes a evaluar
clientes = []

# Se solicita el numero de clientes a evaluar
numClientes = int(input("numero de clientes a evaluar: "))
i = 0

# Ciclo para solitar el monto deacuerdo con los clientes a evaluar
while i < numClientes:
    i += 1
    x = input("Monto de la compra del usuario "+str(i)+" : ")

    # Se agrega el monto a la lista de clientes
    clientes.append(x)


cliente = 1

# Se realiza un ciclo para evaluar los mostos registrados de los clientes
for monto in clientes:
    des = 0
    monto = float(monto)

    # Validacion para el descuento del 30%
    if(monto >= 500):
        des = monto * 0.30

        # Validacion para el descuento del 20%
    elif(monto < 500 and monto >= 200):
        des = monto * 0.20

        # Validacion para el descuento del 10%
    elif(monto < 200 and monto >= 100):
        des = monto * 0.10

        # Impresion en pantalla de los descuentos deacuerdo al cliente
    print("El cliente " + str(cliente) + " Tiene descuento de " + str(des))
    cliente += 1
