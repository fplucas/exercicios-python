vetor = [[], [], []]
for x in range(0, 3):
    print('{}o. vetor: '.format(x + 1))
    for y in range(0, 10):
        valor = input('Entre com o {}o. valor: '.format(y + 1))
        vetor[x].append(valor)

vetor_final = []
for x in range(0, 10):
    for y in range(0, 3):
        vetor_final.append(vetor[y][x])

print(vetor_final)