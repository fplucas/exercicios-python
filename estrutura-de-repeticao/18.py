quantidade = int(input('Quantos números deseja criar? '))
numeros = []
for numero in range(0, quantidade):
    numeros.append(int(input('Entre com o {}o. número: '.format(numero + 1))))

print('O menor número é: {}'.format(min(numeros)))
print('O maior número é: {}'.format(max(numeros)))
print('A soma dos números é: {}'.format(sum(numeros)))