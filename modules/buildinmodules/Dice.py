import random


class Dice:
    def dice_roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        dice = (first, second)
        return dice


dice = Dice()

print(dice.dice_roll())
