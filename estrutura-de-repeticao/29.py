from decimal import Decimal

preco = Decimal('1.99')
print('Loja Quase Dois - Tabela de preços')
for x in range(1, 51):
    print('{} - R$ {}'.format(x, preco * x))