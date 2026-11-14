class Pessoa:
    def __init__(self, sexo, peso, altura):
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura

    def getSexo(self):
        return self.__sexo
    def setSexo(self, sexo):
        self.__sexo = sexo

    def getPeso(self):
        return self.__peso
    def setPeso(self, peso):
        self.__peso = peso

    def getAltura(self):
        return self.__altura
    def setAltura(self, altura):
        self.__altura = altura

    def calcularImc(self):
        imc = self.__peso / (self.__altura ** 2)

        if self.__sexo == 'F':
            if imc < 19.1:
                return 'abaixo do peso'

            elif imc < 25.8:
                return 'no peso normal'

            elif imc < 27.3:
                return 'marginalmente acima do peso'

            elif imc < 32.3:
                return 'acima do peso ideal'
            else:
                return "obeso"

        elif self.__sexo == 'M':
            if imc < 20.7:
                return 'abaixo do peso'

            elif imc < 26.4:
                return 'no peso normal'

            elif imc < 27.8:
                return 'marginalmente acima do peso'

            elif imc < 31.1:
                return 'acima do peso ideal'
            else:
                return "obeso"