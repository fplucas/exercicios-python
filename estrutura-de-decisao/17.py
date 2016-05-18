ano = int(input('Entre com um ano: '))

if(ano % 400 == 0):
    bissexto = True
elif(ano % 100 == 0):
    bissexto = False
elif(ano % 4 == 0):
    bissexto = True
else:
    bissexto = False

if(bissexto):
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))