from decimal import Decimal

def verifica_intervalo(salario):
    if(salario < 1000):
        for x in range(0, 8):
            if(salario >= intervalos[x][0] and salario <= intervalos[x][1]):
                faixas[x] += 1
    else:
        faixas[8] += 1


intervalos = [[200, 299.99], [300, 399.99], [400, 499.99], [500, 599.99], [600, 699.99], [700, 799.99], [800, 899.99], [900, 999.99]]
faixas = [0, 0, 0, 0, 0, 0, 0, 0, 0]
continua = True
print('Digite um valor negativo para encerrar')
while(continua):
    venda_bruta = Decimal(
        input('Venda bruta do {}o. vendedor: '.format(sum(faixas) + 1)))
    if(venda_bruta < 0):
        continua = False
    else:
        salario = venda_bruta * Decimal('0.09') + 200
        verifica_intervalo(salario)

for x in range(0, 8):
    print('Entre $ {} e $ {} = {}'.format(intervalos[x][0], intervalos[x][1], faixas[x]))
print('Acima de $ 1000.00 = {}'.format(faixas[8]))