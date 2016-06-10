numeros = []
for x in range(0, 10):
    numero = float(input('Entre com o {}o. número: '.format(x + 1)))
    numeros.append(numero)

numeros.reverse()
print(numeros)