from math import ceil

class Lata(object):
    'Classe padrão para latas de tinta'
    def __init__(self, metragem_por_litro, capacidade, preco):
        self.metragem_por_litro = metragem_por_litro
        self.capacidade = capacidade
        self.preco = preco

    def calcula_quantidade_de_latas(self, metragem):
        quantidade_de_litros = metragem / self.metragem_por_litro
        quantidade_de_latas = quantidade_de_litros / self.capacidade
        quantidade_de_latas = ceil(quantidade_de_latas)
        return quantidade_de_latas

    def calcula_preco_por_latas(self, quantidade_de_latas):
        preco_total = quantidade_de_latas * self.preco
        return preco_total

print('Quantos metros quadrados deseja pintar?')
metragem = float(input())
lata = Lata(3, 18.0, 80.0)
quantidade_de_latas = lata.calcula_quantidade_de_latas(metragem)
preco = lata.calcula_preco_por_latas(quantidade_de_latas)
print('Serão necessárias %s latas de tinta' % quantidade_de_latas)
print('O que resulta em R$ %s' % preco)