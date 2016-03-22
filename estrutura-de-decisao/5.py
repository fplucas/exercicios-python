def calcula_media(notas):
    media = 0
    for nota in notas:
        print(nota)
        media += nota
    media = media / len(notas)
    return media

notas = []
for nota in range(1, 3):
    notas.append(float(input('Entre com a %s nota: ' % nota)))

media = calcula_media(notas)
print('A média é %s' % media)