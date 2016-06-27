class Carro():
    def __init__(self, consumo):
        self._consumo = consumo
        self._nivel_de_combustivel = 0

    def andar(self, distancia):
        self._nivel_de_combustivel -= distancia / self._consumo

    def obter_gasolina(self):
        return self._nivel_de_combustivel

    def adicionar_gasolina(self, litros):
        self._nivel_de_combustivel += litros