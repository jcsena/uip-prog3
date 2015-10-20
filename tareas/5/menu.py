#
# Copyright (c) 2015 by Julio Seña. All Rights Reserved.
#

#
# [mostrarMenu sirve para carga un menu desde una lista de datos]
# @method mostrarMenu
# @param  {[List]}    menu [Debe contener los parametros de la lista del menu]
# @param  {[String]}    title [Debe contener el titulo del menu]
# @return {[type]}    [Empty]
#
def mostrarMenu(menu, titulo='Titulo'):
    print('____' + titulo + '____')
    num = 1
    for item in menu:
        print(str(num) + '. ' + str(item))
        num += 1
    print()

if __name__ == '__main__':
    mostrarMenu(['test', 'test2', 'test3'], 'SuperTest')
