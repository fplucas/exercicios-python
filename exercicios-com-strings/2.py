nome = input('Entre com o seu nome: ').upper()
letras = list(nome)
letras.reverse()
nome_invertido = ''.join(letras)
print(nome_invertido)