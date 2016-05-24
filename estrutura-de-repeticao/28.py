from decimal import Decimal

quantidade_de_cds = int(input('Quantos cds existem em sua coleção? '))
cds = []
for cd in range(0, quantidade_de_cds):
    preco_invalido = True
    while(preco_invalido):
        preco = Decimal(input(
            'Entre com o valor pago no {}o. cd: '.format(cd + 1)))
        if(preco > 0):
            cds.append(preco)
            preco_invalido = False
        else:
            print('O preço do cd deve ser maior que 0!')

total = sum(cds)
media = total / len(cds)
print('O total gasto em sua coleção é: {}'.format(total))
print('A média de preço dos cds é: {}'.format(media))