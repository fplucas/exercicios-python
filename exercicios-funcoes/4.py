def positivo_ou_negativo(numero):
    if(numero > 0):
        return 'P'
    else:
        return 'N'

numero = int(input('Entre com um número: '))
print(positivo_ou_negativo(numero))