from decimal import Decimal

class Atleta():
    def __init__(self, nome):
        self.nome = nome
        self.saltos = []

    def registra_salto(self, salto):
        self.saltos.append(salto)

    def calcula_media(self):
        media = sum(self.saltos) / len(self.saltos)
        return media

    def imprime_saltos(self):
        print('Saltos: ', end='')
        for salto in self.saltos:
            print('{} '.format(salto), end='')
        print('')

atletas = {}
continua = True
while(continua):
    nome = input('Atleta: ')
    if(nome == ''):
        continua = False
    else:
        atleta = Atleta(nome)
        for x in range(0,5):
            salto = Decimal(input('{}o. salto: '.format(x + 1)))
            atleta.registra_salto(salto)
        atletas[atleta.calcula_media()] = atleta

print('\nResultado final:')
print('Atleta: {}'.format(atletas[max(atletas)].nome))
atletas[max(atletas)].imprime_saltos()
print('Média dos saltos: {} m'.format(atletas[max(atletas)].calcula_media()))