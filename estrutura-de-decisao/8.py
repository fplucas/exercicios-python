produtos = []
for numero in range(1, 4):
    produtos.append(float(input('Informe o preço do %so. produto: ' % numero)))

menor = produtos[0]
for produto in produtos:
    if produto < menor:
        menor = produto

print('O produto que você deve comprar é o de R$ %s' % menor)