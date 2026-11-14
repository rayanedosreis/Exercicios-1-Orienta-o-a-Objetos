from abc import ABC, abstractmethod

class Veiculo(ABC):

    def __init__(self, placa, valorDiario):
        self.__placa = placa
        self.__valorDiario = valorDiario
        self.__alugado = False
        self.__historico = []

    def getPlaca(self):
        return self.__placa

    def getValorDiario(self):
        return self.__valorDiario

    def getAlugado(self):
        return self.__alugado

    @abstractmethod
    def calcularAluguel(self, dias):
        pass

    def alugar(self, cliente, dias):

        if self.__alugado:
            print( f"Veículo de placa {self.__placa} "f"não disponível para aluguel")
            return False

        valor = self.calcularAluguel(dias)

        self.__alugado = True

        self.__historico.append( ("aluguel", cliente.getNome(), valor))

        print(f"Aluguel confirmado para o veículo "f"de placa {self.__placa}")

        return True

    def devolver(self):

        if not self.__alugado:
            print(f"Veículo de placa {self.__placa} "f"não estava alugado")
            return False

        self.__alugado = False

        self.__historico.append(("devolucao",))

        print(f"Devolução realizada para o veículo "f"de placa {self.__placa}")

        return True

    def listarHistorico(self):

        print(f"Histórico do veículo de placa {self.__placa}")

        for registro in self.__historico:

            if registro[0] == "aluguel":
                cliente = registro[1]
                valor = registro[2]

                print( f"Veículo placa {self.__placa} "f"alugado pelo cliente {cliente} "f"no valor de R$ {valor}")

            elif registro[0] == "devolucao":
                print(f"Veículo placa {self.__placa} devolvido")