import calendar
from datetime import datetime
from model.Cargo import Cargo
from model.Ocorrencia import Ocorrencia
from model.Dependente import Dependente

# Associação obrigatória:
# Todo Funcionario possui um Cargo, recebido no construtor.
# Associações opcionais:
# Um Funcionario pode ter zero ou várias Ocorrencias.
# Um Funcionario pode ter zero ou vários Dependentes.
# As listas começam vazias e são preenchidas pelos métodos add.
class Funcionario:

    def __init__(self, nome, cargo):
        self.__nome = nome
        self.__cargo = cargo
        self.__ocorrencias = []
        self.__dependentes = []

    def getNome(self):
        return self.__nome

    def getCargo(self):
        return self.__cargo

    def addOcorrencias(self, ocorrencia):
        self.__ocorrencias.append(ocorrencia)

    def addDependentes(self, dependente):
        self.__dependentes.append(dependente)

    def calcularSalarioLiquido(self, mes, ano):

        salario = self.__cargo.getSalarioBruto()

        for ocorrencia in self.__ocorrencias:
            data = ocorrencia.getData()

            if data.month == mes and data.year == ano:
                salario += ocorrencia.getAcrescimo()
                salario -= ocorrencia.getDesconto()

        ultimoDia = calendar.monthrange(ano, mes)[1]
        dataReferencia = datetime(ano, mes, ultimoDia)

        for dependente in self.__dependentes:
            nascimento = dependente.getDataNascimento()

            idade = ( dataReferencia.year - nascimento.year- ((dataReferencia.month, dataReferencia.day)< (nascimento.month, nascimento.day)))

            if idade < 18:
                salario += 100.0

        return salario