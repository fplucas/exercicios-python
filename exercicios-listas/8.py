idades = []
alturas = []
for x in range(0, 5):
    print('{}a. pessoa'.format(x + 1))
    idade = int(input('Idade: '))
    altura = float(input('Altura: '))
    idades.append(idade)
    alturas.append(altura)

idades.reverse()
alturas.reverse()
for x in range(0, 5):
    print('{}a. pessoa'.format(x + 1))
    print('Idade: ',format(idades[x]))
    print('Altura: ',format(alturas[x]))
