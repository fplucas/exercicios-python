print('Entre com sua altura em metros')
altura = float(input())
print('Qual o seu sexo? m - masculino / f - feminino')
sexo = input()
print('Entre com o seu peso em kgs')
peso = float(input())
if sexo == 'm':
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

if peso > peso_ideal:
    print('Você está acima do peso, seu peso ideal é %s' % peso_ideal)
elif peso < peso_ideal:
    print('Você está abaixo do peso, seu peso ideal é %s' % peso_ideal)
else:
    print('Parabéns, você está em seu peso ideal!')