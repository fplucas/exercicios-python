class Aluno():
    def __init__(self, idade, altura):
        self.idade = idade
        self.altura = altura

def altura_media(alunos):
    soma_altura = 0
    for aluno in alunos:
        soma_altura += aluno.altura
    media = soma_altura / len(alunos)
    return media

alunos = []
for x in range(0, 30):
    print('{}o. aluno'.format(x + 1))
    idade = int(input('Idade: '))
    altura = float(input('Altura: '))
    aluno = Aluno(idade, altura)
    alunos.append(aluno)

media = altura_media(alunos)
total = 0
for aluno in alunos:
    if(aluno.altura < media and aluno.idade > 13):
        total += 1

print('{} alunos têm altura inferior à média e mais de 13 anos.'.format(total))