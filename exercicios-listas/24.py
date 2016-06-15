from random import randrange

def lanca_dado():
    numero = randrange(1, 7, 1)
    return numero

lancamentos = []
for x in range(0, 100):
    lancamentos.append(lanca_dado())

for x in range(1, 7):
    print('Nro. {} foi conseguido {} vezes'.format(x, lancamentos.count(x)))
