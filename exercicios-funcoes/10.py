from random import randrange

def joga_dados():
    return randrange(1, 7, 1)

def obtem_valor():
    valor = 0
    for x in range(0, 2):
        valor += joga_dados()
    print('Valor obtido: {}'.format(valor))
    return valor

natural = [7, 11]
craps = [2, 3, 12]

valor = obtem_valor()
if(valor in natural):
    print('Natural')
    print('Ganhou!')
    exit()
elif(valor in craps):
    print('Craps')
    print('Perdeu!')
    exit()
else:
    ponto = valor
    print('Ponto')
    while(True):
        valor = obtem_valor()
        if(valor == ponto or valor == 7):
            if(valor == ponto):
                print('Ganhou!')
            elif(valor == 7):
                print('Perdeu!')
            break