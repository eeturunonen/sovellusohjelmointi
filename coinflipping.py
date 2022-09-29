import random

class Coin:
    def __init__(self):
        self.sides = "head"
        # self.num = {1 : "head", 0: "tail"}  #this is how I would do this taks..


### 1 = "head", 0 = "tail"
    def toss_coin(self, times):
        i = 0
        while times > i:
            value = random.randint(0,1)
            if value != 0:
                self.sides = "head"
                i += 1
            else:
                self.sides = "tail"
                i += 1
        return self.sides


### In this task I print "head" or "tail" instead of 0 and 1 since it seems more logical