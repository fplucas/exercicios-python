from percentual import calcula_percentual
from conversor import byte_para_megabyte

def le_arquivo():
    arquivo = open('usuarios.txt', 'r')
    conteudo = arquivo.read()
    arquivo.close()
    return conteudo

def obtem_linhas():
    conteudo = le_arquivo()
    linhas = conteudo.split('\n')
    return linhas

def obtem_bytes(linhas):
    bytes = []
    for linha in linhas:
        byte = int(linha[10:].strip())
        bytes.append(byte)
    return bytes

def obtem_nomes(linhas):
    nomes = []
    for linha in linhas:
        nome = linha[:10].strip()
        nomes.append(nome)
    return nomes

def grava_arquivo():
    arquivo = open('relatorio.txt', 'w')
    arquivo.write('Nr. Usuário     Espaço utilizado     % do uso\n')
    for x in range(0, len(bytes)):
        megabyte = byte_para_megabyte(bytes[x])
        percentual = calcula_percentual(bytes[x], sum(bytes))
        arquivo.write('{}   {:12}{:13.2f} MB{:12.2f}%\n'.format(x + 1, nomes[x], megabyte, percentual))

    espaco_total = byte_para_megabyte(sum(bytes))
    arquivo.write('\nEspaço total ocupado: {:.2f} MB\n'.format(espaco_total))
    arquivo.write('Espaço médio ocupado: {:.2f} MB'.format(espaco_total / len(bytes)))
    arquivo.close()

linhas = obtem_linhas()
bytes = obtem_bytes(linhas)
nomes = obtem_nomes(linhas)
grava_arquivo()

"""
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
"""