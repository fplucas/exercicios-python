from decimal import Decimal

salario_atual = Decimal(input('Entre com o seu salário: '))

if salario_atual <= 280.0:
    percentual_aumento = Decimal('20')
elif salario_atual <= 700.0:
    percentual_aumento = Decimal('15')
elif salario_atual <= 1500.0:
    percentual_aumento = Decimal('10')
else:
    percentual_aumento = Decimal('5')

valor_aumento = salario_atual * Decimal(percentual_aumento / 100)
salario_novo = salario_atual + valor_aumento

print('Salário atual: R$ {}'.format(salario_atual))
print('Percentual de aumento: {}%'.format(percentual_aumento))
print('Valor do aumento: R$ {}'.format(valor_aumento))
print('Salário novo: R$ {}'.format(salario_novo))