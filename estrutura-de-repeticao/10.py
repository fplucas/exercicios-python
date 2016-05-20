numeros = []
for numero in range(0, 2):
    numeros.append(int(input('Entre com o {}o. número: '.format(numero + 1))))
if(numeros[0] > numeros[1]):
    print('Intervalo inválido!')
else:
    for numero in range(numeros[0], numeros[1]):
        print(numero)