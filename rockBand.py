from band import Band

class RockBand(Band):
    def __init__(self):
        self.rock_concert_movements = []
    
    def concerts(self, concert):
        self.rock_concert_movements.append(concert)
        return self.rock_concert_movements