class Funcionario():
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    def obter_nome(self):
        return self._nome

    def obter_salario(self):
        return self._salario

    def aumentar_salario(self, porcentagem_de_aumento):
        self._salario += self._salario / 100 * porcentagem_de_aumento