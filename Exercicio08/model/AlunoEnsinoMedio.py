from model.Aluno import Aluno

class AlunoEnsinoMedio(Aluno):
    def aprovado(self):
        return self.calcularMedia() >= 6
