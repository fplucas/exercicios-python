numeros = []
for x in range(0, 10):
    numero = int(input('Entre com o {}o. número: '.format(x + 1)))
    numero = numero ** 2
    numeros.append(numero)

print('Soma dos quadrados: {}'.format(sum(numeros)))