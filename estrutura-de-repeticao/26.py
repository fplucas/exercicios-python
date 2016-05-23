quantidade_de_eleitores = int(input('Entre com a quantidade de eleitores: '))
votos_validos = [1,2,3]
votos = []
for x in range(0, quantidade_de_eleitores):
    voto_invalido = True
    while(voto_invalido):
        voto = int(input(
            '''1 - Candidato 1, 2 - Candidato 2, 3 - Candidato 3
            Entre com o voto do {}o. eleitor: '''.format(x + 1)))
        if(voto in votos_validos):
            votos.append(voto)
            voto_invalido = False
        else:
            print('Favor entrar com voto válido!')

for voto in range(1, 4):
    print('Quantidade de votos do candidato {}: {}'.format(voto, votos.count(voto)))