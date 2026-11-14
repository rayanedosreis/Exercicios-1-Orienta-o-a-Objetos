class ContaBancaria:
    def __init__(self,titular, saldo=0.0):
        self.__titular = titular
        self.__saldo = saldo
        self.__historico = []


    def getTitular(self):
        return self.__titular


    def getSaldo(self):
        return self.__saldo

    def depositar(self, valor):
         if valor <= 0:
            print("Valor invalido")
            return False

         self.__saldo += valor

         self.__historico.append(f"deposito valor de {valor}")
         return True

    def sacar(self, valor):
            if valor <= 0:
                print("Valor invalido")
                return False

            if valor > self.__saldo:
                raise ValueError("Saldo insuficiente")


            self.__saldo -= valor
            self.__historico.append(f"Saque de R$ {valor}")
            return True


    def transferir(self, destino, valor):
        if self.sacar(valor):
            if destino.depositar(valor):
                return True

        return False


    def exibirExtrato(self):
        print(f"Extrato de {self.__titular}")

        for operacao in self.__historico:
            print(operacao)

        print(f"Saldo atual: R$ {self.__saldo}")

