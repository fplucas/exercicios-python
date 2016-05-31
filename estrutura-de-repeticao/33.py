from decimal import Decimal

quantidade = int(input('Entre com a quantidade de temperaturas: '))
temperaturas = []
for temperatura in range(0, quantidade):
    temperaturas.append(Decimal(input(
        '{}a. temperatura: '.format(temperatura + 1))))

media = sum(temperaturas) / len(temperaturas)
print('Menor temperatura: {}'.format(min(temperaturas)))
print('Maior temperatura: {}'.format(max(temperaturas)))
print('Média: {}'.format(media))