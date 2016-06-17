from decimal import Decimal

def valor_pagamento(valor, dias_de_atraso):
    if(dias_de_atraso <= 0):
        prestacao = valor
    else:
        prestacao = valor + valor * Decimal('0.03') + (valor * Decimal('0.001') * dias_de_atraso)
    return prestacao

def relatorio_do_dia(prestacoes):
    print('Quantidade de prestações: {}'.format(len(prestacoes)))
    print('Valor total de prestações: {}'.format(sum(prestacoes)))

prestacoes = []
valor = 1
while(valor != 0):
    valor = Decimal(input('Valor da prestação (0 para encerrar): '))
    if(valor != 0):
        dias_de_atraso = int(input('Dias de atraso: '))
        prestacao = valor_pagamento(valor, dias_de_atraso)
        print('Valor a ser pago: {}'.format(prestacao))
        prestacoes.append(prestacao)

relatorio_do_dia(prestacoes)