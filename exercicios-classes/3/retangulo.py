class Retangulo():
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def altera_lados(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcula_area(self):
        return self.comprimento * self.largura

    def calcula_perimetro(self):
        return (self.comprimento * 2) + (self.largura * 2)

    def obtem_comprimento(self):
        return self.comprimento

    def obtem_largura(self):
        return self.largura