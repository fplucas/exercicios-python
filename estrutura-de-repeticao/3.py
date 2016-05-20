nome_invalido = True
while(nome_invalido):
    nome = input('Entre com o nome: ')
    if(len(nome) <= 3):
        print('O nome deve ter mais de 3 caracteres!')
    else:
        nome_invalido = False

idade_invalida = True
while(idade_invalida):
    idade = int(input('Entre com a idade: '))
    if(idade < 0 or idade > 150):
        print('A idade deve estar entre 0 e 150!')
    else:
        idade_invalida = False

salario_invalido = True
while(salario_invalido):
    salario = float(input('Entre com o salário: '))
    if(salario < 0):
        print('O salário deve ser maior que 0!')
    else:
        salario_invalido = False

sexos_possiveis = ['F', 'M']
sexo_invalido = True
while(sexo_invalido):
    sexo = input('Entre com o sexo. F - Feminino, M - Masculino: ').upper()
    if(sexo not in sexos_possiveis):
        print('Sexo deve ser F - Feminino ou M - Masculino')
    else:
        sexo_invalido = False

estados_civis_possiveis = ['S', 'C', 'V', 'D']
estado_civil_invalido = True
while(estado_civil_invalido):
    estado_civil = input(
        'Entre com o estado civil. S - Solteiro, C - Casado, V - Viúvo, D - Divorciado: ').upper()
    if(estado_civil not in estados_civis_possiveis):
        print('O estado civil deve ser: S - Solteiro, C - Casado, V - Viúvo, D - Divorciado')
    else:
        estado_civil_invalido = False