from decimal import Decimal

def adicao(numeros):
    resultado = numeros[0] + numeros[1]
    return resultado

def subtracao(numeros):
    resultado = numeros[0] - numeros[1]
    return resultado

def multiplicacao(numeros):
    resultado = numeros[0] * numeros[1]
    return resultado

def divisao(numeros):
    resultado = numeros[0] / numeros[1]
    return resultado

def eh_par(numero):
    if(numero % 2 == 0):
        return 'par'
    return 'ímpar'

def eh_positivo(numero):
    if(numero >= 0):
        return 'positivo'
    return 'negativo'

def eh_inteiro(numero):
    if(round(numero) == numero):
        return 'inteiro'
    return 'decimal'

numeros = []
for numero in range(0,2):
    numeros.append(Decimal(input('Entre com o {}o. número: '
        .format(numero + 1))))
opcao = int(input(
'''1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
Qual operação deseja efetuar? '''))

if(opcao == 1):
    resultado = adicao(numeros)
elif(opcao == 2):
    resultado = subtracao(numeros)
elif(opcao == 3):
    resultado = multiplicacao(numeros)
else:
    resultado = divisao(numeros)

par_ou_impar = eh_par(resultado)
positivo_ou_negativo = eh_positivo(resultado)
inteiro_ou_decimal = eh_inteiro(resultado)
print('O resultado {} é {}, {} e {}.'
    .format(resultado, par_ou_impar, positivo_ou_negativo, inteiro_ou_decimal))