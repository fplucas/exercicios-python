numeros = []
for numero in range(0, 5):
    numeros.append(int(input('Entre com o {}o. número: '.format(numero + 1))))

print(max(numeros))