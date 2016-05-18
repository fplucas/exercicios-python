from decimal import Decimal

def calcula_media(notas):
    media = 0
    for nota in notas:
        media += nota
    media /= len(notas)
    return media

notas = []

for nota in range(0, 2):
    notas.append(Decimal(input('Entre com a {}a. nota: '.format(nota + 1))))

media = calcula_media(notas)

if media >= 0 and media < 4:
    conceito = 'E'
elif media < 6:
    conceito = 'D'
elif media < 7.5:
    conceito = 'C'
elif media < 9:
    conceito = 'B'
elif media <= 10:
    conceito = 'A'
else:
    print('Valores inválidos!')
    exit()

for nota in notas:
    print('Nota {}: {}'.format(notas.index(nota) + 1, nota))
print('Média: {}'.format(media))
print('Conceito: {}'.format(conceito))