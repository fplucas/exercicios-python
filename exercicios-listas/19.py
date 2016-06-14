def calcula_percentual(quantidade, total):
    percentual = (quantidade * 100) // total
    return percentual

sistemas_operacionais = {1: 'Windows Server', 2: 'Unix', 3: 'Linux', 4: 'Netware', 5: 'Mac OS', 6: 'Outro'}
votos = []
print('Qual o melhor Sistema Operacional para uso em servidores?\n')
print('As possíveis respostas são:\n')
for numero, sistema_operacional in sistemas_operacionais.items():
    print('{} - {}'.format(numero, sistema_operacional))
continua = True
while(continua):
    voto = int(input('Voto (0 = fim): '))
    if(voto == 0):
        continua = False
    elif(voto >= 1 and voto <= 6):
        votos.append(voto)
    else:
        print('Informe um valor entre 1 e 6 ou 0 para sair!')

print('Sistema Operacional      Votos   %')
print('-------------------      -----   ----')
mais_votado = 0
for numero, sistema_operacional in sistemas_operacionais.items():
    quantidade = votos.count(numero)
    if(quantidade > votos.count(mais_votado)):
        mais_votado = numero
    percentual = calcula_percentual(quantidade, len(votos))
    print('{0:22}   {1:3}     {2:3}%'.format(sistema_operacional, quantidade, percentual))

print('-------------------      -----   ----')
print('Total                      {}'.format(len(votos)))
print('')
print('O Sistema Operacional mais votado foi o {}, com {} votos, correspondendo a {}% dos votos.'.format(sistemas_operacionais[mais_votado], votos.count(mais_votado), calcula_percentual(votos.count(mais_votado), len(votos))))