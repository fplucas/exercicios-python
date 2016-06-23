numeros_por_extenso = {'0': 'Zero', '1': 'Um', '2': 'Dois', '3': 'Três', '4': 'Quatro', '5': 'Cinco', '6': 'Seis', '7': 'Sete', '8': 'Oito', '9': 'Nove', '10': 'Dez', '11': 'Onze', '12': 'Doze', '13': 'Treze', '14': 'Quatorze', '15': 'Quinze', '16': 'Dezesseis', '17': 'Dezessete', '18': 'Dezoito', '19': 'Dezenove', '20': 'Vinte', '30': 'Trinta', '40': 'Quarenta', '50': 'Cinquenta', '60': 'Sessenta', '70': 'Setenta', '80': 'Oitenta', '90': 'Noventa'}

def divide_numero(numero):
    numeros = []
    numeros.append(numero[0] + '0')
    numeros.append(numero[-1])
    return numeros

while(True):
    try:
        numero = input('Entre com um número de 0 a 99: ')
        teste = int(numero)
        if(teste < 0 or teste > 99):
            raise Exception
        break
    except Exception:
        print('Entre com um número válido!')

if(numero in numeros_por_extenso):
    print(numeros_por_extenso[numero])
else:
    numeros = divide_numero(numero)
    print('{} e {}'.format(numeros_por_extenso[numeros[0]], numeros_por_extenso[numeros[1]]))
