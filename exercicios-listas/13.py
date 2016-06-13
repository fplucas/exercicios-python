from decimal import Decimal

meses = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'}
temperaturas = {}
for mes, descricao in meses.items():
    temperatura = Decimal(input('Entre com a temperatura média do mês de {}: '.format(descricao)))
    temperaturas[mes] = temperatura

def calcula_media(temperaturas):
    soma = 0
    for mes, temperatura in temperaturas.items():
        soma += temperatura
    media = soma / len(temperaturas)
    return media

media = calcula_media(temperaturas)
for mes, temperatura in temperaturas.items():
    if(temperatura > media):
        print('{}o. em {}'.format(temperatura, meses[mes]))
