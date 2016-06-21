from random import randrange

def eh_quadrado_magico(matriz):
    eh_quadrado_magico = True
    for x in range(3):
        if(matriz[x] + matriz[x + 3] + matriz[x + 6] != 15):
            eh_quadrado_magico = False
    return eh_quadrado_magico

def imprime_matriz(matriz):
    print(matriz[0:3])
    print(matriz[3:6])
    print(matriz[6:9])

def gera_quadrado_magico():
    matriz = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in range(9):
        novamente = True
        while(novamente):
            numero = randrange(1, 10, 1)
            if(numero not in matriz):
                matriz[x] = numero
                novamente = False
    return matriz

matriz = gera_quadrado_magico()
while(not eh_quadrado_magico(matriz)):
    matriz = gera_quadrado_magico()
    if(eh_quadrado_magico(matriz)):
        imprime_matriz(matriz)
