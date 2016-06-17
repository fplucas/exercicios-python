from datetime import *

def mes_por_extenso(mes):
    meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
    mes_por_extenso = meses[mes]
    return mes_por_extenso

while(True):
    try:
        data = input('Entre com alguma data em formato DD/MM/AAAA: ')
        if(len(data.split('/')) != 3):
            raise Exception
        dia = int(data.split('/')[0])
        mes = int(data.split('/')[1])
        ano = int(data.split('/')[2])
        data = datetime(ano, mes, dia)
        break
    except Exception:
        print('Entre com uma data válida!')

mes_por_extenso = mes_por_extenso(mes)
print('{} de {} de {}'.format(dia, mes_por_extenso, ano))