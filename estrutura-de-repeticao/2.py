usuario = input('Entre com um nome de usuário: ')
senha_invalida = True
while(senha_invalida):
    senha = input('Entre com uma senha: ')
    if(senha == usuario):
        print('A senha não pode ser o nome do usuário.')
    else:
        senha_invalida = False