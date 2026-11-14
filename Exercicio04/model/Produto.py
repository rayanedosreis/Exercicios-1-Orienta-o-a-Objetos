class Produto:
    def __init__(self, nome, qtdeEstoque, minimo, maximo):
        self.__nome = nome
        self.__qtdeEstoque = qtdeEstoque
        self.__minimo = minimo
        self.__maximo = maximo
        self.__historico = []

    def getQuantidadeEstoque(self):
        return self.__qtdeEstoque

    def debitarEstoque(self, quantidade):
        self.__qtdeEstoque -= quantidade

    def creditarEstoque(self, quantidade):
        self.__qtdeEstoque += quantidade

    def verificarEstoqueBaixo(self):
        return self.__qtdeEstoque < self.__minimo

    def verificarEstoqueInsuficiente(self, quantidade):
        return quantidade > self.__qtdeEstoque

    def verificarEstoqueExcedente(self, quantidade):
        return self.__qtdeEstoque + quantidade > self.__maximo

    def vender(self, quantidade):
        if self.verificarEstoqueInsuficiente(quantidade):
            print("Estoque insuficiente")
            return False

        self.debitarEstoque(quantidade)
        self.__historico.append(f"Venda: {quantidade} unidades")

        if self.verificarEstoqueBaixo():
            print("Estoque baixo")

        return True

    def comprar(self, quantidade):
        if self.verificarEstoqueExcedente(quantidade):
            print("Estoque excedente")
            return False

        self.creditarEstoque(quantidade)
        self.__historico.append(f"Compra: {quantidade} unidades")
        return True

    def exibirHistorico(self):
        for registro in self.__historico:
            print(registro)

