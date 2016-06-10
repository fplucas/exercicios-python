from decimal import Decimal

class Atleta():
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def maior_nota(self):
        return max(self.notas)

    def menor_nota(self):
        return min(self.notas)

    def calcula_media(self):
        soma = sum(self.notas)
        media = (soma - self.maior_nota() - self.menor_nota()) / (len(self.notas) - 2)
        return media

    def registra_nota(self, nota):
        self.notas.append(nota)

nome = input('Atleta: ')
atleta = Atleta(nome)
for x in range(0, 7):
    nota = Decimal(input('{}a. Nota: '.format(x + 1)))
    atleta.registra_nota(nota)

print('Resultado final:')
print('Atleta: {}'.format(atleta.nome))
print('Melhor nota: {}'.format(atleta.maior_nota()))
print('Pior nota: {}'.format(atleta.menor_nota()))
print('Média: {}'.format(atleta.calcula_media()))