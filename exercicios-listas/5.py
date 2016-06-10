pares = []
impares = []
numeros = []
for x in range(0, 20):
    numero = int(input('Entre com o {}o. número: '.format(x + 1)))
    numeros.append(numero)
    if(numero % 2 == 0):
        pares.append(numero)
    else:
        impares.append(numero)

print('Números: {}'.format(numeros))
print('Pares: {}'.format(pares))
print('Ímpares: {}'.format(impares))
