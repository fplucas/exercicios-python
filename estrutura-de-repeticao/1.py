valor_invalido = True
while(valor_invalido):
    nota = float(input('Entre com uma nota de zero a dez: '))
    if(nota > 0 and nota < 10):
        valor_invalido = False
    else:
        print('Entre com um valor válido!')