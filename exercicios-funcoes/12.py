from random import shuffle

palavra = input('Palavra: ')
letras = list(palavra)
shuffle(letras)
palavra = ''.join(letras)
print(palavra)