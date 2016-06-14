from decimal import Decimal

print('Projeção de Gastos com Abono')
print('============================')
print('')
salarios = []
continua = True
while(continua):
    salario = Decimal(input('Salário: '))
    if(salario == 0):
        continua = False
    else:
        salarios.append(salario)

abonos_minimos = 0
total_abono = 0
print('\nSalário     -      Abono')
for salario in salarios:
    abono = salario * Decimal('0.2')
    if(abono < 100):
        abono = Decimal('100')
        abonos_minimos += 1
    print('R$ {0:8} - R$ {1:7}'.format(salario, abono))
    total_abono += abono

print('Foram processados {} colaboradores'.format(len(salarios)))
print('Total gasto com abonos: R$ {}'.format(total_abono))
print('Valor mínimo pago a {} colaboradores'.format(abonos_minimos))
print('Maior valor de abono pago: R$ {}'.format(abonos_minimos * 100))