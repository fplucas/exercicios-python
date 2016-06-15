from decimal import Decimal

def valor_gasto(consumo):
    litros = litros_gastos(consumo)
    valor = litros * Decimal('2.25')
    return valor

def litros_gastos(consumo):
    litros = 1000 // consumo
    return litros

def imprime_relatorio_final():
    print('\nRelatório Final')
    for numero, carro in carros.items():
        consumo = consumos[numero]
        litros = litros_gastos(consumos[numero])
        valor = valor_gasto(consumos[numero])
        print('{} - {} - {} - {} litros - R$ {}'.format(numero, carro, consumo, litros, valor))

def imprime_menor_consumo():
    menor_consumo = 1
    for x in range(1, len(carros) + 1):
        if(consumos[x] > consumos[menor_consumo]):
            menor_consumo = x
    print('O menor consumo é do {}'.format(carros[menor_consumo]))

carros = {1: 'Uno', 2: 'Palio', 3: 'Up', 4: 'Ka', 5: 'HB20'}
consumos = {1: Decimal('13.5'), 2: Decimal('13.4'), 3: Decimal('14.8'), 4: Decimal('13.8'), 5: Decimal('13.2')}

for numero, carro in carros.items():
    print('Veículo {}'.format(numero))
    print('Nome: {}'.format(carro))
    print('Km por litro: {}'.format(consumos[numero]))

imprime_relatorio_final()
imprime_menor_consumo()
