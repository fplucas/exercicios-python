from random import randrange

erros = []
chutes = []

def pede_chute():
    chute_invalido = True
    while(chute_invalido):
        chute = input('Digite uma letra: ').upper()
        if(len(chute) == 1):
            chute_invalido = False
    return chute

def valida_chute(chute, palavra):
    if(chute not in palavra):
        erros.append(chute)
        print('Você errou pela {}a. vez. Tente de novo!'.format(len(erros)))
    else:
        acertou_chute(chute, palavra)

def acertou_chute(chute, palavra):
    palavra_com_mascara = ''
    for letra in palavra:
        if(letra in chutes):
            palavra_com_mascara += '{} '.format(letra)
        else:
            palavra_com_mascara += '_ '
    print('A palavra é: {}'.format(palavra_com_mascara))

def obtem_arquivo():
    arquivo = open('palavras.txt', 'r')
    conteudo = arquivo.read()
    palavras = conteudo.split('\n')
    arquivo.close()
    return palavras

def palavra_aleatoria():
    palavras = obtem_arquivo()
    palavra_escolhida = palavras[randrange(1, len(palavras), 1)].upper()
    return palavra_escolhida

def venceu():
    palavra_ok = ''
    for letra in palavra:
        if(letra in chutes):
            palavra_ok += letra
    return palavra == palavra_ok


palavra = palavra_aleatoria()
while(True):
    chute = pede_chute()
    chutes.append(chute)
    valida_chute(chute, palavra)
    if(len(erros) == 6 or venceu()):
        exit()