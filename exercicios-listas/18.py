def calcula_percentual(votos_do_jogador, total_de_votos):
    percentual = (votos_do_jogador * 100) // total_de_votos
    return percentual

file = open('18.txt', 'w')

continua = True
votos = []
while(continua):
    voto = int(input('Número do jogador (0 = fim): '))
    if(voto == 0):
        continua = False
    if(voto >= 1 and voto <= 23):
        votos.append(voto)
    else:
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
print('Resultado da votação:\n')
file.write('Resultado da votação:\n')
print('Foram computados {} votos\n'.format(len(votos)))
file.write('Foram computados {} votos\n'.format(len(votos)))
print('Jogador          Votos            %')
file.write('Jogador          Votos            %\n')
jogador_com_maior_numero_de_votos = 0
for x in range(0, 23):
    if(votos.count(x + 1) != 0):
        jogador = x + 1
        votos_do_jogador = votos.count(jogador)
        if(votos_do_jogador > votos.count(jogador_com_maior_numero_de_votos)):
            jogador_com_maior_numero_de_votos = jogador
        percentual = calcula_percentual(votos_do_jogador, len(votos))
        print('{}                {}                {}%'.format(jogador, votos_do_jogador, percentual))
        file.write('{}                {}                {}%\n'.format(jogador, votos_do_jogador, percentual))

print('O melhor jogador foi o número {}, com {} votos, correspondendo a {}%% do total de votos.'.format(jogador_com_maior_numero_de_votos, votos.count(jogador_com_maior_numero_de_votos), calcula_percentual(votos.count(jogador_com_maior_numero_de_votos), len(votos))))
file.write('O melhor jogador foi o número {}, com {} votos, correspondendo a {}%% do total de votos.'.format(jogador_com_maior_numero_de_votos, votos.count(jogador_com_maior_numero_de_votos), calcula_percentual(votos.count(jogador_com_maior_numero_de_votos), len(votos))))

file.close()
