from funcionario import Funcionario
import unittest

class Funcionario_Test(unittest.TestCase):
    def setUp(self):
        self.funcionario = Funcionario('Juca', 2500)

    def test_funcionario(self):
        self.assertEqual(self.funcionario.obter_nome(), 'Juca')
        self.assertEqual(self.funcionario.obter_salario(), 2500)

if __name__ ==  '__main__':
    unittest.main()