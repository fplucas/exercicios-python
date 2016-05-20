base = int(input('Entre com a base: '))
expoente = int(input('Entre com o expoente: '))

resultado = base
for x in range(1, expoente):
    resultado *= base

print(resultado)