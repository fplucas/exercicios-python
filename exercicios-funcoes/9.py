while True:
    try:
        numero = int(input('Número: '))
        break
    except ValueError:
        print('Entre com um número válido!')

print('{}'.format(str(numero)[::-1]))