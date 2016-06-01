def tabuada(numero, inicio, fim):
    for x in range(inicio, fim + 1):
        resultado = numero * x
        print('{} X {} = {}'.format(numero, x, resultado))

numero = int(input('Montar a tabuada de: '))
intervalo_invalido = True
while(intervalo_invalido):
    inicio = int(input('Começar por: '))
    fim = int(input('Terminar em: '))
    if(inicio >= fim):
        print('Intervalo inválido!')
    else:
        intervalo_invalido = False
tabuada(numero, inicio, fim)
