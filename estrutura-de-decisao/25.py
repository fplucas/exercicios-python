respostas = []
respostas.append(int(input('Telefonou para a vítima? 1 - Sim / 2 - Não: ')))
respostas.append(int(input('Esteve no local do crime? 1 - Sim / 2 - Não: ')))
respostas.append(int(input('Mora perto da vítima? 1 - Sim / 2 - Não: ')))
respostas.append(int(input('Devia para a vítima? 1 - Sim / 2 - Não: ')))
respostas.append(int(input('Já trabalhou com a vítima? 1 - Sim / 2 - Não: ')))

respostas_positivas = 0
for resposta in respostas:
    if(resposta == 1):
        respostas_positivas += 1

if(respostas_positivas == 5):
    print('Assasino')
elif(respostas_positivas >= 3):
    print('Cúmplice')
elif(respostas_positivas == 2):
    print('Suspeita')
else:
    print('Inocente')