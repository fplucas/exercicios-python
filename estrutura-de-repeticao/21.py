numero = int(input('Entre com um número: '))
primo = True
for x in range(2, numero):
    if(numero % x == 0):
        primo = False

if(primo):
    print('O número {} é primo'.format(numero))
else:
    print('O número {} não é primo'.format(numero))