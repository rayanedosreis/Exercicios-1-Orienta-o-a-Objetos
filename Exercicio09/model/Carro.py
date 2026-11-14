from model.Veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, modelo, placa, valorDiario):
        super().__init__(placa, valorDiario)
        self.__modelo = modelo

    def getModelo(self):
        return self.__modelo

    def calcularAluguel(self, dias):
        return self.getValorDiario() * dias