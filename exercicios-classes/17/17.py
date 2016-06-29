from bichinho_virtual import Bichinho_virtual

jedas = Bichinho_virtual('Jedas', 0, 0, 0, 0)
juca = Bichinho_virtual('Juca', 0, 0, 0, 0)
joao = Bichinho_virtual('João', 0, 0, 0, 0)
jonas = Bichinho_virtual('Jonas', 0, 0, 0, 0)
jaco = Bichinho_virtual('Jacó', 0, 0, 0, 0)

def imprimir_menu():
    print('1 - Alterar saúde')
    print('2 - Alterar idade')
    print('3 - Imprimir nome')
    print('4 - Imprimir fome')
    print('5 - Imprimir saúde')
    print('6 - Imprimir idade')
    print('7 - Imprimir humor')
    print('8 - Fornecer comida')
    print('9 - Brincar')

def pede_bichinho():
    for id, bichinho in enumerate(bichinhos):
        print('{} - {}'.format(id, bichinho.retornar_nome()))
    print('{} - Todos'.format(5))
    resposta = int(input('Qual bichinho? '))
    return resposta

def executar_acao(metodo):
    if(resposta >= 1 and resposta <= 4):
        bichinhos[resposta].metodo
    else:
        for bichinho in bichinhos:
            bichinho.metodo

imprimir_menu()
bichinhos = [jedas, juca, joao, jonas, jaco]
while(True):
    acao = input('Entre com a opção desejada (h exibe ajuda): ').upper()
    if(acao == 'H'):
        imprimir_menu()
    elif(acao == '1'):
        resposta = pede_bichinho()
        saude = int(input('Entre com o valor da nova saúde: '))
        if(resposta >= 1 and resposta <= 4):
            bichinhos[resposta].alterar_saude(saude)
        elif(resposta == 5):
            for bichinho in bichinhos:
                bichinho.alterar_saude(saude)
    elif(acao == '2'):
        resposta = pede_bichinho()
        idade = int(input('Entre com a nova idade: '))
        if(resposta >= 1 and resposta <= 4):
            bichinhos[resposta].alterar_idade(idade)
        elif(resposta == 5):
            for bichinho in bichinhos:
                bichinho.alterar_idade(idade)
    elif(acao == '3'):
        resposta = pede_bichinho()
        if(resposta >= 1 and resposta <= 4):
            print(bichinhos[resposta].retornar_nome())
        elif(resposta == 5):
            for bichinho in bichinhos:
                print(bichinho.retornar_nome())
    elif(acao == '4'):
        resposta = pede_bichinho()
        if(resposta >= 1 and resposta <= 4):
            print(bichinhos[resposta].retornar_fome())
        elif(resposta == 5):
            for bichinho in bichinhos:
                print(bichinho.retornar_fome())
    elif(acao == '5'):
        resposta = pede_bichinho()
        if(resposta >= 1 and resposta <= 4):
            print(bichinhos[resposta].retornar_saude())
        elif(resposta == 5):
            for bichinho in bichinhos:
                print(bichinho.retornar_saude())
    elif(acao == '6'):
        resposta = pede_bichinho()
        if(resposta >= 1 and resposta <= 4):
            print(bichinhos[resposta].retornar_idade())
        elif(resposta == 5):
            for bichinho in bichinhos:
                print(bichinho.retornar_idade())
    elif(acao == '7'):
        resposta = pede_bichinho()
        if(resposta >= 1 and resposta <= 4):
            print(bichinhos[resposta].retornar_humor())
        elif(resposta == 5):
            for bichinho in bichinhos:
                print(bichinho.retornar_humor())
    elif(acao == '8'):
        resposta = pede_bichinho()
        comida = int(input('Entre com a quantidade de comida a ser fornecida: '))
        if(resposta >= 1 and resposta <= 4):
            bichinhos[resposta].fornecer_comida(comida)
        elif(resposta == 5):
            for bichinho in bichinhos:
                bichinho.fornecer_comida(comida)
    elif(acao == '9'):
        resposta = pede_bichinho()
        horas = int(input('Entre com a quantidade de horas: '))
        if(resposta >= 1 and resposta <= 4):
            bichinhos[resposta].brincar(horas)
        elif(resposta == 5):
            for bichinho in bichinhos:
                bichinho.brincar(horas)
    elif(acao == '-1'):
        resposta = pede_bichinho()
        if(resposta >= 1 and resposta <= 4):
            str(bichinhos[resposta])
        elif(resposta == 5):
            for bichinho in bichinhos:
                str(bichinho)
    else:
        break