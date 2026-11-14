from model.Veiculo import Veiculo

class Moto(Veiculo):
    def calcularAluguel(self, dias):
        valor = self.getValorDiario() * dias
        if dias < 30:
            valor = valor * 1.20
        else:
            valor = valor * 1.10
        return round(valor, 2)