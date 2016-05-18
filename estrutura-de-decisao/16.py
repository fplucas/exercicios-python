from decimal import Decimal
from math import sqrt

a = Decimal(input('Entre com o valor de a: '))

if(a == 0):
    print('Se o valor de a é 0 a equação não é de segundo grau!')
    exit()

b = Decimal(input('Entre com o valor de b: '))
c = Decimal(input('Entre com o valor de c: '))

delta = b ** 2 - (4 * a * c)

if(delta < 0):
    print('Se o valor de delta é negativo a equação não possui raízes')
    exit()

if(delta == 0):
    raiz = -b / (2 * a)
    print('Como delta é 0, raiz da equação é: {}'.format(raiz))
    exit()

raizes = []
raizes.append((-b + Decimal(sqrt(delta))) / (2 * a))
raizes.append((-b - Decimal(sqrt(delta))) / (2 * a))

for raiz in raizes:
    print('{}a. Raiz: {}'.format(raizes.index(raiz) + 1, raiz))