class TV():
    def __init__(self):
        self.canal = 0
        self.volume = 0

    def aumenta_volume(self):
        if(self.volume < 20):
            self.volume += 1

    def diminui_volume(self):
        if(self.volume > 0):
            self.volume -= 1

    def troca_de_canal(self, canal):
        if(canal > 0 and canal <= 20):
            self.canal = canal