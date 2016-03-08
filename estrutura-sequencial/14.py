peso_maximo = 50
multa_por_quilo = 4.0
print('Entre com o peso')
peso = float(input())
excesso = peso - peso_maximo
if excesso > 0:
    multa = excesso * multa_por_quilo
else:
    excesso = 0
    multa = 0.0
print('O excesso foi de %s kgs' % excesso)
print('A multa foi de R$ %s' % multa)