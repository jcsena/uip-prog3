#
# Copyright (c) 2015 by Julio Seña. All Rights Reserved.
#
'''
El empleador esta celebrando aniversario y ofrecera a sus clientes una serie
de ofertas que se traduciran en incremeno de sus ventas. Las reglas de la
ofertas se basan en un porcentaje de descuento sobre el total de compra, que
estarian variando dependiendo del monto adquirido:

por un monto mayor o igual a $500 -> 30
por un monto menor de $500 y mayor que 200 -> 20
por un monto menor de $200 -> y mayor o igual a $100 -> 10
'''

clientes = []

numClientes = int(input("numero de clientes a evaluar: "))
i = 0

while i < numClientes:
    i += 1
    x = input("Monto de la compra del usuario "+str(i)+" : ")
    clientes.append(x)


len(clientes)
cliente = 1
for monto in clientes:
    des = 0
    monto = float(monto)
    if(monto >= 500):
        des = monto * 0.30
    elif(monto < 500 and monto >= 200):
        des = monto * 0.20
    elif(monto < 200 and monto >= 100):
        des = monto * 0.10
    print("El cliente " + str(cliente) + " Tiene descuento de " + str(des))
    cliente += 1
