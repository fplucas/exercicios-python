numeros = []
for numero in range(1, 4):
    numeros.append(float(input('Entre com o %s número: ' % numero)))

menor = numeros[1]
for numero in numeros:
    if numero < menor:
        menor = numero
print('O menor número é o %s' % menor)