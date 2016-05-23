numero = int(input('Entre com um número: '))
divisivel_por = []
primo = True
for x in range(2, numero):
    if(numero % x == 0):
        primo = False
        divisivel_por.append(x)

if(primo):
    print('O número {} é primo'.format(numero))
else:
    print('O número {} não é primo'.format(numero))
    print('Divisível por:')
    for numero in divisivel_por:
        print(numero)