lados = []

for lado in range(0, 3):
    lados.append(int(input('Entre com o tamanho do {}o. lado: '.format(lado + 1))))

if(lados[0] == lados[1] and lados[1] == lados[2]):
    print('Triângulo equilátero')
elif(lados[0] == lados[1] or lados[1] == lados[2] or lados[0] == lados[2]):
    print('Triângulo isósceles')
else:
    print('Triângulo escaleno')