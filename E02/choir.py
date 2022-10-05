from E02.band import Band

class Choir(Band):
    def __init__(self, band_name, music_genre):
        super().__init__(band_name, music_genre)
        self.size = 0

# Answer to 9th task question "Is there a need for overriding a method? Could overriding also be used with the RockBand class?"
# - Overriding is neccessary if we want to use the same attributes (for example have the name for choir),
#   therefore RockBand needs the same kind of override as in line 5 (RockBand is not done this way at the moment)


    # Tells how many participants are singing in the choir
    def choir_size(self, size):
        self.size = size
        return self.size
        