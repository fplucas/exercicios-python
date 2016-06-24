class Quadrado():
    def __init__(self, lado):
        self.lado = lado

    def altera_lado(self, lado):
        self.lado = lado

    def obtem_lado(self):
        return self.lado

    def calcula_area(self):
        return self.lado ** 2
