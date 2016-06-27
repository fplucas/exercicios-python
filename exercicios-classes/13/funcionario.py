class Funcionario():
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    def obter_nome(self):
        return self._nome

    def obter_salario(self):
        return self._salario