from datetime import datetime
class Dependente:

    def __init__(self, nome, dataNascimento):
        self.__nome = nome
        self.__dataNascimento = dataNascimento

    def getNome(self):
        return self.__nome

    def getDataNascimento(self):
        return self.__dataNascimento