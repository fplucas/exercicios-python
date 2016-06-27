class Conta_de_investimento():
    def __init__(self, saldo, taxa_de_juros):
        self._saldo = saldo
        self._taxa_de_juros = taxa_de_juros

    def adicionar_juros(self):
        self._saldo += self._saldo / 100 * self._taxa_de_juros

    def imprime_saldo(self):
        print('Saldo: {}'.format(self._saldo))

poupanca = Conta_de_investimento(1000, 10)
poupanca.adicionar_juros()
poupanca.adicionar_juros()
poupanca.adicionar_juros()
poupanca.adicionar_juros()
poupanca.adicionar_juros()
poupanca.imprime_saldo()

