from decimal import Decimal

class Candidato():
    def __init__(self, nome):
        self.nome = nome
        self.votos = 0

    def vota(self):
        self.votos += 1

joao = Candidato('João')
jose = Candidato('José')
jonas = Candidato('Jonas')
jedas = Candidato('Jedas')
nulo = Candidato('Votos nulos')
branco = Candidato('Votos em branco')
candidatos = {1: joao, 2: jose, 3: jonas, 4: jedas, 5: nulo, 6: branco}
total_de_votos = 0
votacao = True
voto_invalido = True
while(votacao):
    for candidato in candidatos:
        print('{} - {}'.format(candidato, candidatos[candidato].nome))
    print('0 - Encerra')
    voto = int(input('Entre com o voto: '))
    if(voto == 0):
        votacao = False
    elif(voto in candidatos):
        candidatos[voto].vota()
        total_de_votos += 1
    else:
        print('Voto inválido!')

for candidato in candidatos:
    print(
        '{}: {}'.format(candidatos[candidato].nome, candidatos[candidato].votos))

percentual_nulo = 100 / total_de_votos * candidatos[5].votos
percentual_branco = 100 / total_de_votos * candidatos[6].votos
print('Percentual de votos nulos: {}'.format(percentual_nulo))
print('Percentual de votos em branco: {}'.format(percentual_branco))