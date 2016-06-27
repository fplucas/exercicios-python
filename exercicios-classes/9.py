class Ponto():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def imprimir_valores(self):
        print('x: {}'.format(self._x))
        print('y: {}'.format(self._y))

class Retangulo():
    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura

    def encontrar_centro(self):
        centro = Ponto((self._largura / 2), (self._altura / 2))
        return centro

    def vertice_de_partida(self):
        return Ponto(0, 0)

largura = int(input('Entre com a largura: '))
altura = int(input('Entre com a altura: '))
retangulo = Retangulo(largura, altura)
while(True):
    resposta = input('1 - Alterar valores, 2 - Imprimir Centro, 3 - Sair: ')
    if(resposta == '1'):
        largura = int(input('Entre com a largura: '))
        altura = int(input('Entre com a altura: '))
        retangulo = Retangulo(largura, altura)
    elif(resposta == '2'):
            retangulo.encontrar_centro().imprimir_valores()
    else:
        exit()