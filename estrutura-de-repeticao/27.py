quantidade_de_turmas = int(input('Entre com a quantidade de turmas: '))

quantidade_de_alunos = []
for x in range(0, quantidade_de_turmas):
    quantidade_invalida = True
    while(quantidade_invalida):
        alunos = int(input(
            'Entre com a quantidade de alunos na {}a. turma: '.format(x + 1)))
        if(alunos < 1 or alunos > 40):
            print('As turmas tem de ter entre 1 e 40 alunos!')
        else:
            quantidade_de_alunos.append(alunos)
            quantidade_invalida = False

media = sum(quantidade_de_alunos) / len(quantidade_de_alunos)

print('Média de alunos por turma: {}'.format(media))