from random import randint
from math import ceil

from numpy.random import normal
import itertools as it


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


def skip_i(iterable, i):
    itr = iter(iterable)
    return it.chain(it.islice(itr, 0, i), it.islice(itr, 1, None))


def get_trimmed_or_padded_string(value, width):
    padding_needed = max(width - len(value), 0)
    padding = " "*padding_needed
    return value[:width] + padding
