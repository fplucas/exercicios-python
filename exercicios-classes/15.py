class Bichinho_virtual():
    def __init__(self, nome, fome, saude, idade, tedio):
        self._nome = nome
        self._fome = fome
        self._saude = saude
        self._idade = idade
        self._tedio = tedio

    def alterar_nome(self, nome):
        self._nome = nome

    def alterar_fome(self, fome):
        self._fome = fome

    def alterar_saude(self, saude):
        self._saude = saude

    def alterar_idade(self, idade):
        self._idade = idade

    def retornar_nome(self):
        return self._nome

    def retornar_fome(self):
        return self._fome

    def retornar_saude(self):
        return self._saude

    def retornar_idade(self):
        return self._idade

    def retornar_humor(self):
        return (self._fome + self._saude) / 2

    def fornecer_comida(self, comida):
        self._fome -= comida

    def brincar(self, horas):
        self._tedio -= horas