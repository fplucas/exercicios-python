while True:
    try:
        numero = int(input('Número: '))
        break
    except ValueError:
        print('Entre com um número válido!')

print('{} tem {} dígitos.'.format(numero, len(str(numero))))