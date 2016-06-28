from bichinho_virtual import Bichinho_virtual

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

bichinho_virtual = Bichinho_virtual('Juca', 0, 0, 0, 0)
imprimir_menu()
while(True):
    acao = input('Entre com a opção desejada (h exibe ajuda): ').upper()
    if(acao == 'H'):
        imprimir_menu()
    elif(acao == '1'):
        saude = int(input('Entre com o valor da nova saúde: '))
        bichinho_virtual.alterar_saude(saude)
    elif(acao == '2'):
        idade = int(input('Entre com a nova idade: '))
        bichinho_virtual.alterar_idade(idade)
    elif(acao == '3'):
        print(bichinho_virtual.retornar_nome())
    elif(acao == '4'):
        print(bichinho_virtual.retornar_fome())
    elif(acao == '5'):
        print(bichinho_virtual.retornar_saude())
    elif(acao == '6'):
        print(bichinho_virtual.retornar_idade())
    elif(acao == '7'):
        print(bichinho_virtual.retornar_humor())
    elif(acao == '8'):
        comida = int(input('Entre com a quantidade de comida a ser fornecida: '))
        bichinho_virtual.fornecer_comida(comida)
    elif(acao == '9'):
        horas = int(input('Entre com a quantidade de horas: '))
        bichinho_virtual.brincar(horas)
    elif(acao == '-1'):
        str(bichinho_virtual)
    else:
        break