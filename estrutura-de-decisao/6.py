numeros = []
for numero in range(1, 4):
    numeros.append(float(input('Entre com o %s número: ' % numero)))

maior = 0
for numero in numeros:
    if numero > maior:
        maior = numero
print('O maior número é o %s' % maior)