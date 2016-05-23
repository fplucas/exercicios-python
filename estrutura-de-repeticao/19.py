quantidade = int(input('Quantos números deseja criar? '))
numeros = []
for numero in range(0, quantidade):
    numero_invalido = True
    while(numero_invalido):
        valor = int(input('Entre com o {}o. número: '.format(numero + 1)))
        if(valor >= 0 and valor <= 1000):
            numeros.append(valor)
            numero_invalido = False
        else:
            print('O número deve estar entre 0 e 1000')

print('O menor número é: {}'.format(min(numeros)))
print('O maior número é: {}'.format(max(numeros)))
print('A soma dos números é: {}'.format(sum(numeros)))