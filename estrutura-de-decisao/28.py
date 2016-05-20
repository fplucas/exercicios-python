from decimal import Decimal

class Carne(object):
    def __init__(self, nome, preco_ate_5kg, preco_acima_de_5kg):
        self.nome = nome
        self.preco_ate_5kg = preco_ate_5kg
        self.preco_acima_de_5kg = preco_acima_de_5kg

    def calcula_preco(self, kilos):
        if(kilos > 5):
            preco = self.preco_acima_de_5kg * kilos
        else:
            preco = self.preco_ate_5kg * kilos
        return preco

def imprime_cupom(carne, kilos, preco_bruto, desconto, forma_de_pagamento, preco_liquido):
    print('''
        Produto: {}
        Quantidade: {}
        Valor Total: {}
        Tipo de Pagamento: {}
        Desconto: {}
        Valor a pagar: {}'''
        .format(carne.nome, kilos, preco_bruto, forma_de_pagamento, desconto, preco_liquido))

print('''
Tabela de preços          Até 5 Kg       Acima de 5 Kg
1 - Filé Duplo      R$ 4,90 por Kg      R$ 5,80 por Kg
2 - Alcatra         R$ 5,90 por Kg      R$ 6,80 por Kg
3 - Picanha         R$ 6,90 por Kg      R$ 7,80 por Kg''')
opcao = int(input('Qual carne deseja comprar? '))
if(opcao == 1):
    carne = Carne('Filé Duplo', Decimal('4.9'), Decimal('5.8'))
elif(opcao == 2):
    carne = Carne('Alcatra', Decimal('5.9'), Decimal('6.8'))
elif(opcao == 3):
    carne = Carne('Picanha', Decimal('6.9'), Decimal('7.8'))
else:
    print('Valor inválido!')
    exit()
kilos = Decimal(input(
    'Quantos kilos de {} deseja comprar? '.format(carne.nome)))
preco_bruto = carne.calcula_preco(kilos)
cartao_tabajara = input(
    'A compra será feita no cartão Tabajara? S - Sim / N - Não: ').upper()
if(cartao_tabajara == 'S'):
    desconto = preco_bruto / 100 * 5
    forma_de_pagamento = 'Cartão Tabajara'
else:
    desconto = Decimal('0')
    forma_de_pagamento = 'Dinheiro'

preco_liquido = preco_bruto - desconto
imprime_cupom(carne, kilos, preco_bruto, desconto, forma_de_pagamento, preco_liquido)