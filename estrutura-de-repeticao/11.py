numeros = []
for numero in range(0, 2):
    numeros.append(int(input('Entre com o {}o. número: '.format(numero + 1))))

if(numeros[0] > numeros[1]):
    print('Intervalo inválido!')
else:
    soma = 0
    while(numeros[0] < numeros[1]):
        soma = soma + numeros[0]
        numeros[0] += 1

    print('Soma: {}'.format(soma))