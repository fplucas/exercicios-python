numero = int(input('Entre com um número: '))

fatorial = 1
for x in range(0, numero):
    fatorial *= (x + 1)

print('{} fatorial é {}'.format(numero, fatorial))