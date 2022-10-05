from dog import Dog
from E02.band import Band
from rockBand import RockBand
from choir import Choir
from coinflipping import Coin

### This section is for Dog class test runs ####

dog1 = Dog("Karri", 2, "Red")     # Task 2
dog1.bark()




### This section is for Band class test runs ###


band = Band("TESTI", "TESTIMUSA")     # Task 4

band.describe_band()
band.is_activce(False)
band.is_activce(True)


###---------------------- This part is for task 5 ----------------------###


apulanta = Band("Apulanta", "Rock")
centralcee = Band("Central Cee", "UK Rap")
lauritahka = Band("Lauri Tähkä", "Pop")

apulanta.describe_band()
centralcee.describe_band()
lauritahka.describe_band()

band = Band("TESTI", "TESTIMUSA")


###---------------------- This part is for task 6 ----------------------###


print(f"{band.band_name} has won {band.home_awards} home awards")
band.home_awards += 2
print(f"{band.band_name} has won {band.home_awards} home awards")
print(f"{band.band_name} has won {band.international_awards} international awards")
band.international_awards += 5
print(f"{band.band_name} has won {band.international_awards} international awards")


###---------------------- This part is for task 7 ----------------------###


band.set_home_awards(4)
print(f"{band.band_name} has won {band.home_awards} home awards")
band.set_international_awards(10)
print(f"{band.band_name} has won {band.international_awards} international awards")


###---------------------- This part is for task 8 ----------------------###


rockBand = RockBand()

rockBand.concerts("The basic head bob")
rockBand.concerts("the one-armed fist pump,")
rockBand.concerts("the up and down jumping motion")
print(rockBand.rock_concert_movements)


###---------------------- This part is for task 9 ----------------------###


choir = Choir("Pahuksen Papat", "Choir")

choir.choir_size(15)
print(f"The choir {choir.band_name} size is {choir.size} members")


###---------------------- This part is for task 10 ----------------------###


coin = Coin()

print(coin.toss_coin(10))
print(coin.toss_coin(20))
print(coin.toss_coin(50))

