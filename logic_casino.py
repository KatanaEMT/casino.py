import random


class GameLogic:

    def Game(self, price, word):
        slots = list(range(1, 31))
        chance = random.choice(slots)
        if chance == word:
            return price * 2
        else:
            return -price
