def tabuada(numero, inicio, fim):
    for x in range(inicio, fim + 1):
        resultado = numero * x
        print('{} X {} = {}'.format(numero, x, resultado))

numero = int(input('Montar a tabuada de: '))
inicio = int(input('Começar por: '))
fim = int(input('Terminar em: '))
tabuada(numero, inicio, fim)
