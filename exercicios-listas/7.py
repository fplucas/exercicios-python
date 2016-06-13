def multiplicacao(numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

numeros = []
for x in range(0, 5):
    numero = int(input('Entre com o {}o. número: '.format(x + 1)))
    numeros.append(numero)

print('Números: {}'.format(numeros))
print('Soma: {}'.format(sum(numeros)))
print('Multiplicação: {}'.format(multiplicacao(numeros)))