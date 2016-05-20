def tabuada(numero):
    for x in range(1, 11):
        resultado = numero * x
        print('{} X {} = {}'.format(numero, x, resultado))

numero = int(input('Entre com um número de 1 a 10: '))
if(numero >= 1 and numero <= 10):
    tabuada(numero)
else:
    print('Valor inválido!')