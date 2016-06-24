import random

def embaralha_palavra(palavra):
    return ''.join(random.sample(palavra, len(palavra)))

def obtem_arquivo():
    arquivo = open('palavras.txt', 'r')
    conteudo = arquivo.read()
    palavras = conteudo.split('\n')
    arquivo.close()
    return palavras

def obtem_palavra():
    palavras = obtem_arquivo()
    palavra_escolhida = palavras[random.randrange(1, len(palavras), 1)].upper()
    return palavra_escolhida

erros = []
palavra = obtem_palavra()
palavra_embaralhada = embaralha_palavra(palavra)
while(True):
    print('Palavra embaralhada: {}'.format(palavra_embaralhada))
    chute = input('Tentativa {}: '.format(len(erros) + 1)).upper()
    if(chute == palavra):
        print('Você venceu! A palavra era {}'.format(palavra))
        exit()
    else:
        print('Errou!')
        erros.append(chute)
    if(len(erros) == 6):
        print('Perdeu o jogo!')
        exit()