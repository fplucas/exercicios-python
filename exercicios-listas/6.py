from decimal import Decimal

medias = []
for x in range(0, 10):
    print('{}o. aluno'.format(x + 1))
    notas = []
    for y in range(0, 4):
        nota = Decimal(input('Entre com a {}a. nota: '.format(y + 1)))
        notas.append(nota)
    media = sum(notas) / len(notas)
    medias.append(media)

for media in medias:
    if(media >= 7):
        print('Média: {}'.format(media))