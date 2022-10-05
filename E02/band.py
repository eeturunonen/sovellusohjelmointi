class Band:         # Task 3
    def __init__(self, band_name, music_genre):
        self.band_name = band_name
        self.music_genre = music_genre
        self.home_awards = 0                # Task 6
        self.international_awards = 0       # Task 6


        
    def describe_band(self):
        print(f"Band name is {self.band_name} and the genre is {self.music_genre}.")


    def is_activce(self, status):
        if status == True:
            print(f"The band is currently active")
        else:
            print(f"The band is currently not active")
    
    def set_home_awards(self, awards):              # Task 7
        self.home_awards = awards

    def set_international_awards(self, awards):     # Task 7
        self.international_awards = awards