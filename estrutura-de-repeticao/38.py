from decimal import Decimal

salario = Decimal(input('Salário inicial: '))
aumento = Decimal('1.5')

for x in range(1995, 2016):
    salario = salario + (salario / 100 * aumento)
    aumento *= 2

print('Salário em 2016: {}'.format(salario))