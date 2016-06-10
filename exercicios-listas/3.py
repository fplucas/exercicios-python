from decimal import Decimal

notas = []
for x in range(0, 4):
    nota = Decimal(input('Entre com a {}a. nota: '.format(x + 1)))
    notas.append(nota)

for x in range(0, len(notas)):
    print('Nota {}: {}'.format(x + 1, notas[x]))

media = sum(notas) / len(notas)
print('Média: {}'.format(media))