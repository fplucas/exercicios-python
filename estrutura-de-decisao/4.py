vogais = ('a', 'e', 'i', 'o', 'u')
letra = input('Entre com uma letra: ').lower()
if letra in vogais:
    print('%s é uma vogal' % letra)
else:
    print('%s é uma consoante' % letra)