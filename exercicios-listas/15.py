from decimal import Decimal

def informa_quantidade_de_notas(notas):
    print('Quantidade de notas: {}'.format(len(notas)))

def informa_notas(notas):
    print('Notas:', end=' ')
    for nota in notas:
        print(nota, end=' ')
    print('')

def informa_notas_invertidas(notas):
    print('Notas invertidas:')
    notas.reverse()
    for nota in notas:
        print(nota)

def calcula_soma(notas):
    return sum(notas)

def calcula_media(notas):
    media = calcula_soma(notas) / len(notas)
    return media

def informa_soma(notas):
    soma = calcula_soma(notas)
    print('Soma das notas: {}'.format(soma))

def informa_media(notas):
    media = calcula_media(notas)
    print('Média das notas: {}'.format(media))

def calcula_notas_acima_da_media(notas):
    media = calcula_media(notas)
    notas_acima_da_media = 0
    for nota in notas:
        if(nota > media):
            notas_acima_da_media += 1
    return notas_acima_da_media

def informa_quantidade_de_notas_acima_da_media(notas):
    notas_acima_da_media = calcula_notas_acima_da_media(notas)
    print('Quantidade de notas acima da média: {}'.format(notas_acima_da_media))

def informa_quantidade_de_notas_abaixo_de_sete(notas):
    notas_abaixo_de_7 = 0
    for nota in notas:
        if(nota < 7):
            notas_abaixo_de_7 += 1
    print('Quantidade de notas abaixo de 7: {}'.format(notas_abaixo_de_7))

continua = True
notas = []
while(continua):
    nota = Decimal(input('Nota: '))
    if(nota == -1):
        continua = False
    else:
        notas.append(nota)

informa_quantidade_de_notas(notas)
informa_notas(notas)
informa_notas_invertidas(notas)
informa_soma(notas)
informa_media(notas)
informa_quantidade_de_notas_acima_da_media(notas)
informa_quantidade_de_notas_abaixo_de_sete(notas)
print('Fim')