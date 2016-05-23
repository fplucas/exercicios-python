from decimal import Decimal

quantidade_de_notas = int(input('Entre com a quantidade de notas: '))

notas = []
for nota in range(0, quantidade_de_notas):
    notas.append(Decimal(input('Entre com a {}a. nota: '.format(nota + 1))))

media = sum(notas) / len(notas)
print('A média de notas é: {}'.format(media))