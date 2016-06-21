print('Compara duas strings')
string1 = input('String 1: ')
string2 = input('String 2: ')
print('Tamanho de "{}": {}'.format(string1, len(string1)))
print('Tamanho de "{}": {}'.format(string2, len(string2)))
if(len(string1) != len(string2)):
    print('As duas strings são de tamanhos diferentes.')
else:
    print('As duas strings são de tamanhos iguais.')
    if(string1 == string2):
        print('As duas strings possuem conteúdo igual.')
    else:
        print('As duas strings possuem conteúdo diferente.')