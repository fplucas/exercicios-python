from decimal import Decimal

class Populacao(object):
    def __init__(self, populacao, taxa_de_crescimento):
        self.populacao = populacao
        self.taxa_de_crescimento = taxa_de_crescimento

    def passa_ano(self):
        self.populacao = self.populacao + (self.populacao / 100 * self.taxa_de_crescimento)

populacao_a = Populacao(Decimal('80000'), Decimal('3'))
populacao_b = Populacao(Decimal('200000'), Decimal('1.5'))

anos_passados = 0
while(populacao_a.populacao < populacao_b.populacao):
    populacao_a.passa_ano()
    populacao_b.passa_ano()
    anos_passados += 1

print('{} anos foram passados.'.format(anos_passados))