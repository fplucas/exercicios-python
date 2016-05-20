from decimal import Decimal

print('''
Tabela de preços          Até 5 Kg     Acima de 5 Kg
Morango             R$ 2,50 por Kg    R$ 2,20 por Kg
Maçã                R$ 1,80 por Kg    R$ 1,50 por Kg''')
kilos_morango = Decimal(input('Quantos quilos de morango deseja comprar? '))
kilos_maca = Decimal(input('Quantos quilos de maçã deseja comprar? '))

if(kilos_morango <= 5):
    preco_morango = Decimal('2.5') * kilos_morango
else:
    preco_morango = Decimal('2.2') * kilos_morango

if(kilos_maca <= 5):
    preco_maca = Decimal('1.8') * kilos_maca
else:
    preco_maca = Decimal('1.5') * kilos_maca

preco_total = preco_morango + preco_maca
if(preco_total > 25 or (kilos_maca + kilos_morango > 8)):
    preco_total = preco_total - (preco_total / 100 * 10)

print('Valor a ser pago: R$ {}'.format(preco_total))