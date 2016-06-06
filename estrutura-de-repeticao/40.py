cidades_menos_de_2000 = 0
soma_de_acidentes = 0
total_de_veiculos = 0
total_de_acidentes = 0
for x in range(0, 5):
    codigo = int(input('Código da cidade: '))
    veiculos = int(input('Número de veículos em 1999: '))
    acidentes = int(input(
        'Número de acidentes de trânsito com vítimas em 1999: '))
    if(x == 0):
        maior_indice = acidentes
        menor_indice = acidentes
        codigo_maior_indice = codigo
        codigo_menor_indice = codigo
    if(acidentes > maior_indice):
        maior_indice = acidentes
        codigo_maior_indice = codigo
    if(acidentes < menor_indice):
        menor_indice = acidentes
        codigo_menor_indice = codigo
    if(veiculos < 2000):
        total_de_acidentes += acidentes
        cidades_menos_de_2000 += 1
    total_de_veiculos += veiculos

if(cidades_menos_de_2000 != 0):
    media_acidentes = total_de_acidentes / cidades_menos_de_2000
else:
    media_acidentes = 0

media_veiculos = total_de_veiculos / 5

print('''Maior índice de acidente de trânsito
    Código: {}
    Quantidade de veículos: {}'''.format(codigo_maior_indice, maior_indice))
print('''Menor índice de acidente de trânsito
    Código: {}
    Quantidade de veículos: {}'''.format(codigo_menor_indice, menor_indice))
print('Média de veículos: {}'.format(media_veiculos))
print('Média de acidentes em cidades com menos de 2000 veículos: {}'.format(media_acidentes))