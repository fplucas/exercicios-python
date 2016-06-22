vogais = ['A', 'E', 'I', 'O', 'U']
espacos_em_branco = 0
quantidade_de_vogais = 0
frase = input('Frase: ').upper()
for letra in frase:
    if(letra == ' '):
        espacos_em_branco += 1
    elif(letra in vogais):
        quantidade_de_vogais += 1

print('Quantidade de espaços em branco: {}'.format(espacos_em_branco))
print('Quantidade de vogais: {}'.format(quantidade_de_vogais))