from decimal import Decimal

valor_hora = Decimal(input('Entre com o valor da sua hora: '))
horas_trabalhadas = Decimal(input('Entre com as horas trabalhadas no mês: '))

salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    porcentagem_ir = 0
elif salario_bruto <= 1500:
    porcentagem_ir = 5
elif salario_bruto <= 2500:
    porcentagem_ir = 10
else:
    porcentagem_ir = 20

valor_ir = salario_bruto / 100 * porcentagem_ir
valor_inss = salario_bruto / 100 * 10
valor_fgts = salario_bruto / 100 * 11
total_de_descontos = valor_ir + valor_inss
salario_liquido = salario_bruto - total_de_descontos

print('Salário Bruto: ({} * {}) : R$ {}'.format(valor_hora, horas_trabalhadas, salario_bruto))
print('(-) IR ({}%) : R$ {}'.format(porcentagem_ir, valor_ir))
print('(-) INSS (10%) : R$ {}'.format(valor_inss))
print('FGTS (11%) : R$ {}'.format(valor_fgts))
print('Total de descontos : R$ {}'.format(total_de_descontos))
print('Salário Líquido: R$ {}'.format(salario_liquido))