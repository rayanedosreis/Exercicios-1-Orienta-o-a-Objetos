class Turma:
    def __init__(self, nome, professor, disciplina):
        self.__nome = nome
        self.__professor = professor
        self.__disciplina = disciplina
        self.__alunos = []

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getProfessor(self):
        return self.__professor

    def setProfessor(self, professor):
        self.__professor = professor

    def getDisciplina(self):
        return self.__disciplina

    def setDisciplina(self, disciplina):
        self.__disciplina = disciplina

    def getAlunos(self):
        return self.__alunos.copy()

    def addAluno(self, aluno):
        if aluno not in self.__alunos:
            self.__alunos.append(aluno)

    def nomeProfessor(self):
        return self.__professor.getNome()

    def nomesAlunos(self):
        return [aluno.getNome() for aluno in self.__alunos]

    def alunoEstaNaTurma(self, aluno):
        return aluno in self.__alunos

    def removeAluno(self, aluno):
        if aluno in self.__alunos:
            self.__alunos.remove(aluno)

    def __str__(self):
        return self.__nome