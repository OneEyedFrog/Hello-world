import random


def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    roll = (dice1 , dice2)
    print("dice rolled: {} and {}".format(dice1, dice2))


roll_dice()