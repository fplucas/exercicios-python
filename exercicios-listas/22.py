def calcula_percentual(quantidade):
    percentual = quantidade * 100 // sum(mouses)
    return percentual

situacoes = {1: 'Necessita da esfera', 2: 'Necessita de limpeza', 3: 'Necessita troca do cabo ou conector', 4: 'Quebrado ou inutilizado'}
continua = True
mouses = [0, 0, 0, 0]
while(continua):
    situacao = int(input('Situação: '))
    if(situacao == 0):
        continua = False
    elif(situacao in situacoes):
        mouses[situacao - 1] += 1
    else:
        print('Informe um valor entre 1 e 4 ou 0 para sair!')

print('Quantidade de mouses: {}'.format(sum(mouses)))
print('\nSituação                                   Quantidade      Percentual')
for x in range(1, 5):
    percentual = calcula_percentual(mouses[x - 1])
    print('{} - {:36} {:12} {:14}%'.format(x, situacoes[x], mouses[x - 1], percentual))