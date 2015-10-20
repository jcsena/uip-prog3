'''

'''
import os.path

class Hola(object):
    __contador = 0
    """docstring for Hola"""
    def __init__(self, message=""):
        super(Hola, self).__init__()
        self.message = message
        Hola.__contador += 1
    '''
    /**
     * [mostrar_contador retorna el contador de clases instanciadas]
     * @method mostrar_contador
     * @param  {[Object]}         self [this de la clase]
     * @return {[int]}         [Contador __contador]
     */
    '''
    def mostrar_contador(self):
        return self.__contador
    '''
    /**
     * [comparar_message compara el mensaje que contiene el atributo mesaje con "Hola Mundo"]
     * @method comparar_message
     * @param  {[Object]}         self       [this de la clase]
     * @param  {[String]}         message="" [Mensaje de validacion]
     * @return {[String]}         [Retorna si es igual el mensaje]
     */
    '''
    def comparar_message(self, message=""):
        hola = "Hola Mundo"
        if(len(hola) == len(self.message)):
            if(self.message.upper() == hola.upper()):
                return "Letras iguales"
            else:
                return "Letras no iguales not match " + self.message
        else:
            return "Letras no iguales largo"

    '''
     * [guardar
        crea un archivo de de log si no existe.
        Lee los mensajes guardados y agrega el message
        de la clase en ese momento
        ]
     * @method guardar
     * @param  {[object]} self [this de la clase]
     * @return {[null]}
     *
    '''
    def guardar(self):
        fname = "log.txt"

        # valida que arhivo este creado
        if(not os.path.isfile(fname)):

            # Se crea el archivo de log
            out_file = open(fname, "wt")
            out_file.close()

        # Se crea una lista que contendra todos los mensajes
        messages = []
        in_file = open(fname, "rt")
        # Se leen todos los mensajes del log
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
