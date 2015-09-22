
'''
calcular el area y perimetro de un rectangulo dada la base y la altura
de 5 cm y 7 cm respectivamente ademas debe convertir los resultados del area y perimetro a metros y pulgadas
'''

#se definen las variables de base y altura
base = 5;
altura = 7;

#se calcula el area
area = base * altura;

#se calcula perimetro
perimetro = (base * 2) + (altura * 2)

#se converiter el area a metros
areaToMetro  = area/100

#se convierte el area a pulgadas
areaToPulaga = area/2.54

#se convierte el perimetro a metros
perimetroToMetro = perimetro/100

#se convierte el perimetro a pulgadas
perimetroToPulaga = perimetro/2.54


# se imprimen los resultados
print("area en centimetros = " + str(area) + " cm")
print("perimetro en centimetros = " + str(perimetro) + " cm")

print("area a metros = " + str(areaToMetro) + " m")
print("area a pulgadas = " + str(areaToPulaga) + " pul")

print("perimetro en metros" + str(perimetroToMetro) + " m")
print("perimetro en pulgadas" + str(perimetroToPulaga) + " pul")
