class Cargo:

    def __init__(self, nome, salarioBruto):
        self.__nome = nome
        self.__salarioBruto = salarioBruto

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getSalarioBruto(self):
        return self.__salarioBruto

    def setSalarioBruto(self, salarioBruto):
        self.__salarioBruto = salarioBruto