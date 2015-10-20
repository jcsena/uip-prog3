import unittest


def imprimirLista(lista, titulo='titulo'):
    print('____' + titulo + '____')
    n = 1
    for l in lista:
        print(str(n) + '. ' + l)
        n += 1
    print()

def agregarLista(lista, item):
    if(item != ''):
        lista.append(item)

def eliminarLita(lista, item):
    i = 0
    for it in lista:
        if (it == item):
            del lista[i]
            break
        i += 1

def editarLista(lista, item, remp):
    i = 0
    for it in lista:
        if (it == item):
            lista[i] = remp
            break
        i += 1

if __name__ == '__main__':
    unittest.main()
