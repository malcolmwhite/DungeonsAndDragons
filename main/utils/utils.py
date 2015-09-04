from random import randint
from math import ceil

from numpy.random import normal


# noinspection PyNoneFunctionAssignment
def generate_attribute(center_value, spread):
    if spread == 0:
        return center_value
    attribute = normal(center_value, spread)
    # noinspection PyTypeChecker
    return int(ceil(attribute))


def simulate_chance(percent_chance_success):
    dice_roll = randint(0, 99)
    return dice_roll < percent_chance_success


def raise_(ex):
    raise ex
