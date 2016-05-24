from decimal import Decimal

preco = Decimal('0.18')
print('Preço do pão: R$ {}'.format(preco))
print('Panificadora Pão de Ontem - Tabela de preços')
for x in range(1, 51):
    print('{} - R$ {}'.format(x, preco * x))