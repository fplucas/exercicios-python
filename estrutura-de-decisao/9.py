numeros = []
for numero in range(1,4):
    numeros.append(float(input('Entre com o %so. número: ' % numero)))

numeros.sort()
for numero in numeros:
    print(numero)
