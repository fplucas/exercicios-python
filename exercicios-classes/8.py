class Macaco():
    def __init__(self, nome):
        self._nome = nome
        self._bucho = []

    def comer(self, alimento):
        self._bucho.append(alimento)

    def ver_bucho(self):
        print(self._bucho)

    def digerir(self, alimento):
        self._bucho.remove(alimento)