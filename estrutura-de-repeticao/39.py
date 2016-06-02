alunos = []
for x in range(0, 10):
    numero = int(input('Número do {}o. aluno: '.format(x + 1)))
    altura = int(input('Altura em centímetros: '))
    if(x == 0):
        maior_altura = altura
        menor_altura = altura
    if(altura > maior_altura):
        maior_altura = altura
        maior_aluno = numero
    if(altura < menor_altura):
        menor_altura = altura
        menor_aluno = numero

print('''Maior aluno
    Número: {}
    Altura: {}'''.format(maior_aluno, maior_altura))
print('''Menor aluno
    Número: {}
    Altura: {}'''.format(menor_aluno, menor_altura))
