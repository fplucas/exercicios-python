numero = int(input('Entre com um número: '))
x = 1
y = x
for y in range(1, numero + 1):
    print('{}/{} = {}'.format(x, y, x/y))
