calcular_novamente = 'S'
while(calcular_novamente == 'S'):
    numero_invalido = True
    while(numero_invalido):
        numero = int(input('Entre com um número: '))
        if(numero >= 0 and numero <= 16):
            fatorial = 1
            for x in range(0, numero):
                fatorial *= (x + 1)

            print('{} fatorial é {}'.format(numero, fatorial))
            numero_invalido = False
        else:
            print('O número deve estar entre 0 e 16')
    calcular_novamente = input('Deseja calcular novamente? S/N: ').upper()