consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
vogais = ['a', 'e', 'i', 'o', 'u']
letras = consoantes + vogais
caracteres = []
for x in range(0, 10):
    caractere = '  '
    while(len(caractere) > 1):
        caractere = input('Entre com o {}o. caractere: '.format(x + 1))
        if(caractere not in letras):
            print('Digite um caractere válido!')
        elif(caractere in consoantes):
            caracteres.append(caractere)

print('{} consoantes'.format(len(caracteres)))
print(caracteres)