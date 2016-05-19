from decimal import Decimal

saque = Decimal(input('Qual o valor que deseja sacar? Mín: 10 Máx: 600: '))
if(saque < 10 or saque > 600):
    print('O saque tem de estar dentro dos limites!')
    exit()

notas_de_100 = saque // 100
resto = saque % 100
notas_de_50 = resto // 50
resto = resto % 50
notas_de_10 = resto // 10
resto = resto % 10
notas_de_5 = resto // 5
resto = resto % 5
notas_de_1 = resto

print('Notas de 100: {}'.format(notas_de_100))
print('Notas de 50 : {}'.format(notas_de_50))
print('Notas de 10 : {}'.format(notas_de_10))
print('Notas de 5  : {}'.format(notas_de_5))
print('Notas de 1  : {}'.format(notas_de_1))