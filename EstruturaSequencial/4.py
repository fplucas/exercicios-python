print('Vamos calcular a média das notas')
soma_das_notas = 0
for bimestre in range(1, 5):
    print('Informe a nota do %so. bimestre' % bimestre)
    nota = int(input())
    soma_das_notas += nota
media = soma_das_notas / 4
print('A média das notas é de %s' % media)