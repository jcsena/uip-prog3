
import hola as h
import menu as m


if __name__ == '__main__':
    menu = ['Igr. Message', 'Comparar', 'Guardar', 'Mostrar Contador', 'Salir']
    while True:
        m.mostrarMenu(menu, 'Comparar Hola')
        try:
            opm = int(input("Opcion (1-" + str(len(menu)) + "): "))
        except:
            print("Opcion no valida")
        else:
            if opm == 1:
                message = input("Ingresa el mensaje por favor: ")
                hello = h.Hola(message)
                print("Mesaje ingreaso " + message)
            elif opm == 2:
                try:
                    res = hello.comparar_message()
                    print(res)
                except:
                    print("Por favor ingrese el mensaje")
            elif opm == 3:
                try:
                    hello.guardar()
                except:
                    print("Por favor ingrese el mensaje")

            elif opm == 4:
                try:
                    print(hello.mostrar_contador())
                except:
                    print("Por favor ingrese el mensaje")
            elif opm == 5:
                break
            else:
                print("Opcion no valida")
                mostrarMenu()

    print("Hasta luego!")
    # test = h.Hola("Hola Mundo")
    # b = test.comparar_message("Hola Mundo")
    # test.guardar()
    # print(b)
