class Curso:
    def __init__(self, nome):
        self.__nome = nome
        self.__turmas = []

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getTurmas(self):
        return self.__turmas.copy()

    def addTurma(self, turma):
        if turma not in self.__turmas:
            self.__turmas.append(turma)

    def nomesAlunos(self):
        nomes = []

        for turma in self.__turmas:
            for nome in turma.nomesAlunos():
                if nome not in nomes:
                    nomes.append(nome)

        return nomes

    def nomesDisciplinas(self):
        nomes = []

        for turma in self.__turmas:
            nome = turma.getDisciplina().getNome()

            if nome not in nomes:
                nomes.append(nome)

        return nomes

    def alunoEstaNoCurso(self, aluno):
        for turma in self.__turmas:
            if turma.alunoEstaNaTurma(aluno):
                return True

        return False

    def removeTurma(self, turma):
        if turma in self.__turmas:
            self.__turmas.remove(turma)

    def __str__(self):
        return self.__nome