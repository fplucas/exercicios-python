gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A']
possiveis_respostas = ['A', 'B', 'C', 'D', 'E']
alunos = []
continua = 'S'
while(continua == 'S'):
    print('{}o. aluno'.format(len(alunos) + 1))
    acertos = 0
    for x in range(0, 10):
        resposta = 'X'
        while(resposta not in possiveis_respostas):
            resposta = input('{}a. resposta: '.format(x + 1)).upper()
            if(resposta not in possiveis_respostas):
                print('Entre com uma resposta válida! A, B, C, D ou E')
            else:
                if(resposta == gabarito[x]):
                    acertos += 1
    alunos.append(acertos)
    continua = input('Continua? s/n: ').upper()

print('Maior acerto: {}'.format(max(alunos)))
print('Menor acerto: {}'.format(min(alunos)))
print('Total de alunos: {}'.format(len(alunos)))
print('Média de acertos: {}'.format(sum(alunos) / len(alunos)))