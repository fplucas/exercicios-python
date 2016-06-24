import re

def numero_invalido(numero):
    return len(numero) != 7

print('Valida e corrige número de telefone')
numero = ''
while(True):
    try:
        numero = input('Telefone: ')
        numero = ''.join(re.findall('\d', numero))
        if(numero_invalido(numero)):
            raise Exception
        break
    except Exception:
        print('Entre com um número de 7 dígitos!')

telefone_corrigido = '3' + numero
print('Telefone possui 7 dígitos. Vou acrescentar o dígito três na frente.')
print('Telefone corrigido sem formatação: {}'.format(telefone_corrigido))
print('Telefone corrigido com formatação: {}-{}'.format(telefone_corrigido[:4], telefone_corrigido[4:]))