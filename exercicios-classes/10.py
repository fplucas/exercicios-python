class Bomba_de_combustivel():
    def __init__(self, tipo_de_combustivel, valor_litro, quantidade_de_combustivel):
        self._tipo_de_combustivel = tipo_de_combustivel
        self._valor_litro = valor_litro
        self._quantidade_de_combustivel = quantidade_de_combustivel

    def abastecer_por_valor(self, valor):
        quantidade_abastecida = valor / self._valor_litro
        self._quantidade_de_combustivel -= quantidade_abastecida
        print('Foi abastecido {} litros'.format(quantidade_abastecida))

    def abastecer_por_litro(self, litros):
        valor_a_pagar = self._valor_litro * litros
        self._quantidade_de_combustivel -= litros
        print('O valor a pagar é R$ {}'.format(valor_a_pagar))

    def alterar_valor(self, valor):
        self._valor_litro = valor

    def alterar_combustivel(self, combustivel):
        self._tipo_de_combustivel = combustivel

    def alterar_quantidade_de_combustivel(self, quantidade):
        self._quantidade_de_combustivel = quantidade