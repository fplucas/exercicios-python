from decimal import Decimal

notas = []
for nota in range(0, 3):
    notas.append(Decimal(input('Entre com a {}a. nota: '.format(nota + 1))))

def calcula_media(notas):
    media = Decimal('0')
    for nota in notas:
        media += nota
    media /= len(notas)
    return media

media = calcula_media(notas)
if(media == 10):
    print('Aprovado com distinção! Nota {}!'.format(media))
elif(media >= 7):
    print('Aprovado! Nota {}!'.format(media))
else:
    print('Reprovado! Nota {}'.format(media))