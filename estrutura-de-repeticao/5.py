from decimal import Decimal

class Populacao(object):
    def __init__(self, populacao, taxa_de_crescimento):
        self.populacao = populacao
        self.taxa_de_crescimento = taxa_de_crescimento

    def passa_ano(self):
        self.populacao = self.populacao + (self.populacao / 100 * self.taxa_de_crescimento)

populacao = Decimal(input('Entre com a população A: '))
taxa_de_crescimento = Decimal(input('Entre com a taxa de crescimento: '))
populacao_a = Populacao(Decimal(populacao), Decimal(taxa_de_crescimento))
populacao = Decimal(input('Entre com a população B: '))
taxa_de_crescimento = Decimal(input('Entre com a taxa de crescimento: '))
populacao_b = Populacao(Decimal(populacao), Decimal(taxa_de_crescimento))

anos_passados = 0
while(populacao_a.populacao < populacao_b.populacao):
    populacao_a.passa_ano()
    populacao_b.passa_ano()
    anos_passados += 1

print('{} anos foram passados.'.format(anos_passados))