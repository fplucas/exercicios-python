numero = int(input('Entre com um número inteiro menor que 1000: '))

if(numero >= 1000):
    print('O número deve ser menor que 1000!')
    exit()

centenas = numero // 100
resto_centenas = numero % 100
dezenas = resto_centenas // 10
unidades = resto_centenas % 10

if(centenas == 1):
    texto_centenas = '{} centena'.format(centenas)
else:
    texto_centenas = '{} centenas'.format(centenas)

if(dezenas == 1):
    texto_dezenas = '{} dezena'.format(dezenas)
else:
    texto_dezenas = '{} dezenas'.format(dezenas)

if(unidades == 1):
    texto_unidades = '{} unidade'.format(unidades)
else:
    texto_unidades = '{} unidades'.format(unidades)

print('{}, {} e {}.'.format(texto_centenas, texto_dezenas, texto_unidades))