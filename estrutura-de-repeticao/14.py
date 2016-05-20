numeros = []
for numero in range(0, 10):
    numeros.append(int(input('Entre com o {}o. número: '.format(numero + 1))))

numeros_pares = 0
numeros_impares = 0
for numero in numeros:
    if(numero % 2 == 0):
        numeros_pares += 1
    else:
        numeros_impares += 1

print('{} números pares'.format(numeros_pares))
print('{} números ímpares'.format(numeros_impares))