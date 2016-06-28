from funcionario import Funcionario
import unittest

class Funcionario_Test(unittest.TestCase):
    def setUp(self):
        self.funcionario = Funcionario('Juca', 2500)

    def testar_nome_do_funcionario(self):
        self.assertEqual(self.funcionario.obter_nome(), 'Juca')

    def testar_salario_do_funcionario(self):
        self.assertEqual(self.funcionario.obter_salario(), 2500)

    def testar_aumento_de_salario(self):
        self.funcionario.aumentar_salario(10)
        self.assertEqual(self.funcionario.obter_salario(), 2750)

if __name__ ==  '__main__':
    unittest.main()