from datetime import datetime

data_informada = input('Entre com uma data no formato dd/mm/aaaa: ')
data = data_informada.rsplit('/')
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])

try:
    data_valida = datetime(ano, mes, dia)
except ValueError:
    data_valida = None

if(data_valida):
    print('A data informada é válida!')
else:
    print('A data informada é inválida!')