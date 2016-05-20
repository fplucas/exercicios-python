from decimal import Decimal

def concede_desconto(valor, porcentagem):
    return valor - (valor / 100 * porcentagem)


combustivel = input(
    'Com qual combustível deseja abastecer? A - Álcool / G - Gasolina: '
    ).upper()
if(combustivel == 'A'):
    preco_combustivel = Decimal('1.90')
    desconto_abaixo_de_20l = 3
    desconto_acima_de_20l = 5
elif(combustivel == 'G'):
    preco_combustivel = Decimal('2.50')
    desconto_abaixo_de_20l = 4
    desconto_acima_de_20l = 6
else:
    print('Valor inválido!')
    exit()

litros = Decimal(input('Quantos litros?'))


preco_bruto = litros * preco_combustivel
if(litros > 20):
    preco_liquido = preco_bruto - (preco_bruto / 100 * desconto_acima_de_20l)
else:
    preco_liquido = preco_bruto - (preco_bruto / 100 * desconto_abaixo_de_20l)

print('O preço a ser pago é: R$ {}'.format(preco_liquido))