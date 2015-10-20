'''

'''
import os.path

class Hola(object):
    __contador = 0
    """docstring for hola"""
    def __init__(self, message=""):
        super(Hola, self).__init__()
        self.message = message
        Hola.__contador += 1

    def mostrar_contador(self):
        return self.__contador

    def comparar_message(self, message=""):
        hola = "Hola Mundo"
        if(len(hola) == len(self.message)):
            if(self.message.upper() == hola.upper()):
                return "Letras iguales"
            else:
                return "Letras no iguales not match " + self.message
        else:
            return "Letras no iguales largo"

    def guardar(self):
        fname = "log.txt"

        if(not os.path.isfile(fname)):
            out_file = open(fname, "wt")
            out_file.close()
        messages = []
        in_file = open(fname, "rt")
        while True:
            in_line = in_file.readline()
            if not in_line:
                break
            in_line = in_line[:-1]
            contador, message = in_line.split(",")
            messages.append([contador, message])
        in_file.close()
        messages.append([str(self.__contador), self.message])
        out_file = open(fname, "wt")
        for mgs in messages:
            out_file.write(mgs[0] + "," + mgs[1] + "\n")
        out_file.close()
