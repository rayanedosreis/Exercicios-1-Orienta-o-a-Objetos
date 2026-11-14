import unittest
from model.Pessoa import Pessoa

class TestePessoa(unittest.TestCase):

    def testMulherAbaixoDoPessoa(self):
        pessoa = Pessoa("F", 19.0, 1.0)
        self.assertEqual(pessoa.calcularImc(),"abaixo do peso" )

    def testMulherLimitePesoNormal(self):
        pessoa = Pessoa("F", 19.1, 1.0)
        self.assertEqual(pessoa.calcularImc(), "no peso normal")

    def testMulherAbaixoLimiteMarginal(self):
        pessoa = Pessoa("F", 25.7, 1.0)
        self.assertEqual(pessoa.calcularImc(), "no peso normal")

    def testMulherLimiteMarginal(self):
        pessoa = Pessoa("F", 25.8, 1.0)
        self.assertEqual(pessoa.calcularImc(),"marginalmente acima do peso")

    def testMulherAbaixoLimiteAcimaIdeal(self):
        pessoa = Pessoa("F", 27.2, 1.0)
        self.assertEqual(pessoa.calcularImc(),"marginalmente acima do peso")

    def testMulherLimiteAcimaIdeal(self):
        pessoa = Pessoa("F", 27.3, 1.0)
        self.assertEqual(pessoa.calcularImc(), "acima do peso ideal")

    def testMulherAbaixoLimiteObeso(self):
        pessoa = Pessoa("F", 32.2, 1.0)
        self.assertEqual(pessoa.calcularImc(), "acima do peso ideal")

    def testMulherLimiteObeso(self):
        pessoa = Pessoa("F", 32.3, 1.0)
        self.assertEqual(pessoa.calcularImc(), "obeso")


    def testHomemAbaixoDoPeso(self):
        pessoa = Pessoa("M", 20.6, 1.0)
        self.assertEqual(pessoa.calcularImc(), "abaixo do peso")

    def testHomemLimitePesoNormal(self):
        pessoa = Pessoa("M", 20.7, 1.0)
        self.assertEqual(pessoa.calcularImc(), "no peso normal")

    def testHomemAbaixoLimiteMarginal(self):
        pessoa = Pessoa("M", 26.3, 1.0)
        self.assertEqual(pessoa.calcularImc(), "no peso normal")

    def testHomemLimiteMarginal(self):
        pessoa = Pessoa("M", 26.4, 1.0)
        self.assertEqual(pessoa.calcularImc(),"marginalmente acima do peso")

    def testHomemAbaixoLimiteAcimaIdeal(self):
        pessoa = Pessoa("M", 27.7, 1.0)
        self.assertEqual(pessoa.calcularImc(),"marginalmente acima do peso")

    def testHomemLimiteAcimaIdeal(self):
        pessoa = Pessoa("M", 27.8, 1.0)
        self.assertEqual(pessoa.calcularImc(), "acima do peso ideal")

    def testHomemAbaixoLimiteObeso(self):
        pessoa = Pessoa("M", 31.0, 1.0)
        self.assertEqual(pessoa.calcularImc(), "acima do peso ideal")

    def testHomemLimiteObeso(self):
        pessoa = Pessoa("M", 31.1, 1.0)
        self.assertEqual(pessoa.calcularImc(), "obeso")


if __name__ == '__main__':
    unittest.main()