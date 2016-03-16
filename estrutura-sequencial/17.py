from math import ceil

class Lata(object):
    'Classe padrão para latas de tinta'
    def __init__(self, metragem_por_litro, capacidade, preco):
        self.metragem_por_litro = metragem_por_litro
        self.capacidade = capacidade
        self.preco = preco
        self.rendimento = metragem_por_litro * capacidade

    def calcula_quantidade_de_latas(self, metragem):
        quantidade_de_litros = metragem / self.metragem_por_litro
        quantidade_de_latas = quantidade_de_litros / self.capacidade
        quantidade_de_latas = ceil(quantidade_de_latas)
        return quantidade_de_latas

    def calcula_preco_por_latas(self, quantidade_de_latas):
        preco_total = quantidade_de_latas * self.preco
        return preco_total

    def informa_quantidade_de_latas(self, metragem):
        quantidade_de_latas = self.calcula_quantidade_de_latas(metragem)
        print('Serão necessárias %s latas de tinta de %s litros' % (quantidade_de_latas, self.capacidade))

    def informa_preco(self, metragem):
        quantidade_de_latas = self.calcula_quantidade_de_latas(metragem)
        preco = self.calcula_preco_por_latas(quantidade_de_latas)
        print('O que resulta em R$ %s' % preco)

def distribui_latas(metragem, lata_grande, lata_pequena):
    quantidade_de_latas_grandes = 0
    quantidade_de_latas_pequenas = 0
    metragem *= 1.1
    while metragem > 0:
        if metragem > lata_pequena.rendimento:
            quantidade_de_latas_grandes += 1
            metragem -= lata_grande.rendimento
        else:
            quantidade_de_latas_pequenas += 1
            metragem -= lata_pequena.rendimento
    print('Serão necessárias %s latas grandes, o que resulta em R$ %s' % (quantidade_de_latas_grandes, lata_grande.calcula_preco_por_latas(quantidade_de_latas_grandes)))
    print('Serão necessárias %s latas pequenas, o que resulta em R$ %s' % (quantidade_de_latas_pequenas, lata_pequena.calcula_preco_por_latas(quantidade_de_latas_pequenas)))

print('Quantos metros quadrados deseja pintar?')
metragem = float(input())
lata_grande = Lata(3, 18.0, 80.0)
lata_pequena = Lata(3, 3.6, 25.0)
lata_grande.informa_quantidade_de_latas(metragem)
lata_grande.informa_preco(metragem)
lata_pequena.informa_quantidade_de_latas(metragem)
lata_pequena.informa_preco(metragem)
distribui_latas(metragem, lata_grande, lata_pequena)