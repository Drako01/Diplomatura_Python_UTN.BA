class AccesoPrivado(object):

    def __privado(self):
        print("Método privado ")

    def getPrivado(self):
        self.__privado()

objeto = AccesoPrivado()
objeto.getPrivado()
objeto._AccesoPrivado__privado()





