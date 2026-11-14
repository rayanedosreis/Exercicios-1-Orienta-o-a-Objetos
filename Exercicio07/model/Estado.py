class Estado:

    def __init__(self, nome, pais):
        self.__nome = nome
        self.__pais = pais

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getPais(self):
        return self.__pais

    def setPais(self, pais):
        self.__pais = pais