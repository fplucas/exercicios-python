from decimal import *
getcontext().prec = 2

valor_da_divida = Decimal(input('Entre com o valor da dívida: '))
print('Valor da dívida Valor dos Juros Quantidade de parcelas Valor da parcela')
print('{}             0               1                      {}'.format(valor_da_divida, valor_da_divida))
quantidade_de_parcelas = 0
porcentagem_juros = 0
for x in range(0,4):
    quantidade_de_parcelas += 3
    porcentagem_juros += 5
    valor_dos_juros = valor_da_divida / 100 * porcentagem_juros
    valor_da_divida_com_juros = valor_da_divida + valor_dos_juros
    valor_da_parcela = valor_da_divida_com_juros / quantidade_de_parcelas
    print('{}             {}               {}                      {}'.format(valor_da_divida_com_juros, valor_dos_juros, quantidade_de_parcelas, valor_da_parcela))
