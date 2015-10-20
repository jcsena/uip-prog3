'''
# TAREA

*Fecha de Revisión*: 19/10/2015

## Instrucciones:
1. Usted fue contratado por la startup ABC como programador.
Ellos le solicitan que programe la primera fase de un
módulo que represente una lista de supermercados. El programa
debe presentar un menú donde pueda elegir, por lo poco, si quiero
agregar, eliminar y ver los elementos de mi lista de supermercado.
Se pueden manejar hasta 3 listas de supermercado. ABC está interesada en
funciones, manejo de excepciones y módulos. Este código debe servir
para posteriores proyectos.
 '''
import menu
import funciones as fun

menuItems = ['Motrar Lista',
             'Agregar',
             'Eliminar',
             'Editar',
             'Salir']

def mostrarMenu():
    menu.mostrarMenu(menuItems, 'Lista Super')


if __name__ == '__main__':
    listSuper = []
    while True:
        mostrarMenu()
        try:
            opm = int(input("Opcion (1-" + str(len(menuItems)) + "): "))
        except:
            print("Opcion no valida")
        else:
            if opm == 1:
                fun.imprimirLista(listSuper, '****_Mi Lista_***')
            elif opm == 2:
                item = input("Agrega a la lista: ")
                fun.agregarLista(listSuper, item)
            elif opm == 3:
                item = input("Eliminar de la lista: ")
                fun.eliminarLita(listSuper, item)
            elif opm == 4:
                item = input("Editar de la lista: ")
                remp = input("Remplazar por: ")
                fun.editarLista(listSuper, item, remp)
            elif opm == 5:
                break
            else:
                print("Opcion no valida")
                mostrarMenu()

    print("Hasta luego!")
