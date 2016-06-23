import re

def calcula_proximo_digito(cpf):
    resultados = []
    for posicao, valor in enumerate(cpf):
        peso = len(cpf) + 1 - posicao
        resultados.append(peso * int(valor))
    resto = sum(resultados) % 11
    if(resto > 1):
        return str(11 - resto)
    else:
        return '0'

def remove_mascara(cpf):
    cpf_sem_mascara = ''.join(re.findall('\d', cpf))
    if(len(cpf_sem_mascara) != 11):
        raise Exception
    return cpf_sem_mascara

def valida_cpf(cpf):
    cpf_calculado = cpf[:9]
    cpf_calculado += calcula_proximo_digito(cpf_calculado)
    cpf_calculado += calcula_proximo_digito(cpf_calculado)
    return cpf == cpf_calculado

while(True):
    try:
        cpf = input('Digite um CPF no formato xxx.xxx.xxx-xx: ')
        cpf = remove_mascara(cpf)
        break
    except Exception:
        print('Entre com um formato válido!')

cpf_valido = valida_cpf(cpf)
if(cpf_valido):
    print('O CPF informado é válido!')
else:
    print('O CPF informado é inválido!')