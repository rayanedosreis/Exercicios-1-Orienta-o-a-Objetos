from model.Aluno import Aluno


class AlunoGraduacao(Aluno):
    def aprovado(self):
        return self.calcularMedia() >= 7
