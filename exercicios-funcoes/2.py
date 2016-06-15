numero = int(input('Entre com um número: '))
for x in range(1, numero + 1):
    linha = ''
    for y in range(0, x):
        linha += '{} '.format(x)
    print(linha)