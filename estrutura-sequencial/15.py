# -*- coding: utf-8 -*-

print('Quanto vale a sua hora?')
salario_por_hora = float(input())
print('Quantas horas você trabalha por mês?')
horas_trabalhadas_por_mes = int(input())
salario = salario_por_hora * horas_trabalhadas_por_mes
valor_imposto_de_renda = salario * 0.11
valor_inss = salario * 0.08
valor_sindicato = salario * 0.05
impostos = valor_imposto_de_renda + valor_inss + valor_sindicato
salario_liquido = salario - impostos
print(' + Salário Bruto: R$ %s ' % salario)
print(' - IR (11%%): R$ %s ' % valor_imposto_de_renda)
print(' - INSS (8%%): R$ %s ' % valor_inss)
print(' - Sindicato (5%%): R$ %s ' % valor_sindicato)
print(' = Salário Líquido: R$ %s ' % salario_liquido)
