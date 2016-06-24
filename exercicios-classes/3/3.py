from decimal import Decimal
from retangulo import Retangulo

def obtem_local():
    comprimento = Decimal(input('Entre com o comprimento do local: '))
    largura = Decimal(input('Entre com a largura do local: '))
    return Retangulo(comprimento, largura)

def obtem_piso():
    comprimento = Decimal(input('Entre com o comprimento do piso: '))
    largura = Decimal(input('Entre com a largura do piso: '))
    return Retangulo(comprimento, largura)

local = obtem_local()
piso = obtem_piso()
quantidade_de_pisos = local.calcula_area() / piso.calcula_area()
quantidadade_de_rodapes = local.calcula_perimetro() / piso.calcula_perimetro()
print('Quantidade de pisos: {}'.format(quantidade_de_pisos))
print('Quantidade de rodapés: {}'.format(quantidadade_de_rodapes))