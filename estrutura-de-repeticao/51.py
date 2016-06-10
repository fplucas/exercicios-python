numero = int(input('Entre com um número: '))
for x in range(1, numero + 1):
    if(x == 1):
        y = 1
    print('{}/{} = {}'.format(x, y, x/y))
    y += 2
