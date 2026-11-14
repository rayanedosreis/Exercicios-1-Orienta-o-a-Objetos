# Associações obrigatórias:
# Toda Cidade possui um Estado, e todo Estado possui um Pais.
# Essas associações são recebidas nos construtores de Cidade e Estado.
# Associações opcionais:
# A Pessoa pode não ter cidade de nascimento nem escolaridade.
# Nesse caso, os atributos recebem None.
class Pessoa:

    def __init__(self, nome, cidade=None):
        self.__nome = nome
        self.__cidade = cidade
        self.__escolaridade = None

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getCidade(self):
        return self.__cidade

    def setCidade(self, cidade):
        self.__cidade = cidade

    def getEscolaridade(self):
        return self.__escolaridade

    def setEscolaridade(self, escolaridade):
        self.__escolaridade = escolaridade

    def cidadeNascimento(self):
        if self.__cidade is None:
            return "Não informado"

        return self.__cidade.getNome()

    def estadoNascimento(self):
        if self.__cidade is None:
            return "Não informado"

        return self.__cidade.getEstado().getNome()

    def paisNascimento(self):
        if self.__cidade is None:
            return "Não informado"

        return self.__cidade.getEstado().getPais().getNome()

    def escolaridadeDescricao(self):
        if self.__escolaridade is None:
            return "Não informado"

        return self.__escolaridade.getDescricao()