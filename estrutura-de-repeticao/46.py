from decimal import Decimal

class Atleta():
    def __init__(self, nome):
        self.nome = nome
        self.saltos = []

    def registra_salto(self, salto):
        self.saltos.append(salto)

    def maior_salto(self):
        return max(self.saltos)

    def menor_salto(self):
        return min(self.saltos)

    def media_saltos(self):
        media = (sum(self.saltos) - self.maior_salto() - self.menor_salto()) / (len(self.saltos) - 2)
        return media

    def exibe_informacoes(self):
        print('\nAtleta: {}'.format(self.nome))
        print('Melhor salto: {} m'.format(self.maior_salto()))
        print('Pior salto: {} m'.format(self.menor_salto()))
        print('Média dos demais saltos: {} m'.format(self.media_saltos()))

nome = '.'
atletas = {}
while(nome != ''):
    nome = input('\nAtleta: ')
    if(nome != ''):
        atleta = Atleta(nome)
        for x in range(0, 5):
            salto = Decimal(input('{}o. salto: '.format(x + 1)))
            atleta.registra_salto(salto)
        atleta.exibe_informacoes()
        atletas[atleta.media_saltos()] = atleta.nome

print('\nResultado final:')
print('{}: {} m'.format(atletas[max(atletas)], max(atletas)))