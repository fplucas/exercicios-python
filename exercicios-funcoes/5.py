from decimal import Decimal

def soma_imposto(custo, taxa_imposto):
    valor_com_imposto = custo + (custo / Decimal('100') * taxa_imposto)
    return valor_com_imposto

custo = Decimal(input('Custo: '))
taxa_imposto = Decimal(input('Taxa de imposto: '))
valor_com_imposto = soma_imposto(custo, taxa_imposto)
print('Valor com imposto: {:.2f}'.format(valor_com_imposto))