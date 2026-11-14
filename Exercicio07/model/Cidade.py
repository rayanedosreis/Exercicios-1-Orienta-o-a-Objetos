class Cidade:

    def __init__(self, nome, estado):
        self.__nome = nome
        self.__estado = estado

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getEstado(self):
        return self.__estado

    def setEstado(self, estado):
        self.__estado = estado