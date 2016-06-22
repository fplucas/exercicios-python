nome = input('Entre com o nome: ').upper()
for letra in range(len(nome), 0, -1):
    print(nome[0:letra])