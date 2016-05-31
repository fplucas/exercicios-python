from decimal import Decimal

compra = []
valor_item = -1
print('Lojas Tabajara')
while(valor_item != 0):
    valor_item = Decimal(input(
        'Produto {}: R$ '.format(len(compra) + 1)))
    if(valor_item > 0):
        compra.append(valor_item)

print('Total: R$ {}'.format(sum(compra)))
recebido = Decimal(input('Dinheiro: R$ '))
troco = recebido - sum(compra)
print('Troco: R$ {}'.format(troco))