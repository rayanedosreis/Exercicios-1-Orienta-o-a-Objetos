from datetime import datetime, timedelta
from model.Dependente import Dependente

class Funcionario:
    def __init__(self, nome):
        self.__nome = nome
        self.__dependentes = []

    def addDependentes(self, dependente):
        self.__dependentes.append(dependente)

    def proximoAniversario(self, dependente, dataAtual):
        nascimento = dependente.getdataNascimento()

        aniversario = datetime(dataAtual.year,nascimento.month,nascimento.day)

        if aniversario.date() < dataAtual.date():
            aniversario = aniversario.replace(year=dataAtual.year + 1)

        return aniversario

    def diasParaAniversario(self, dependente, dataAtual):
        aniversario = self.proximoAniversario(dependente, dataAtual)
        return (aniversario.date() - dataAtual.date()).days

    def diaSemanaAniversario(self, dependente, dataAtual):
        aniversario = self.proximoAniversario(dependente, dataAtual)

        diasSemana = ["Segunda-feira","Terça-feira","Quarta-feira","Quinta-feira","Sexta-feira","Sábado","Domingo"]

        return diasSemana[aniversario.weekday()]

    def listarDependentes(self, dataAtual):
        print(f"Dependentes de {self.__nome}")

        for dependente in self.__dependentes:
            nascimento = dependente.getdataNascimento()
            aniversario = self.proximoAniversario(dependente, dataAtual)

            dias = self.diasParaAniversario(dependente, dataAtual)
            diaSemana = self.diaSemanaAniversario(dependente, dataAtual)

            print(f"{dependente.getNome()} | " f"nascimento: {nascimento.strftime('%d/%m/%Y')} | "f"próximo aniversário: {aniversario.strftime('%d/%m/%Y')} | "f"faltam {dias} dias | {diaSemana}")
