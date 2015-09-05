from random import randint
from math import ceil
import itertools as it

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


def skip_i(iterable, i):
    itr = iter(iterable)
    return it.chain(it.islice(itr, 0, i), it.islice(itr, 1, None))


def get_trimmed_or_padded_string(value, width):
    padding_needed = max(width - len(value), 0)
    padding = " " * padding_needed
    return value[:width] + padding


def get_padded_attribute(instance, attribute, cell_width):
        value = getattr(instance, attribute)()
        value = value.splitlines()
        result = ""
        for line in value:
            result += get_trimmed_or_padded_string(line, cell_width) + "\n"
        return result[:-1]


def join_multi_line_strings(blocks, cell_width):
        output = ""
        while blocks:
            left = blocks.pop()
            right = blocks.pop() if blocks else ""
            left = left.splitlines()
            right = right.splitlines()
            if_missing = " " * cell_width
            for left_line, right_line in it.izip_longest(left, right, fillvalue=if_missing):
                output += left_line + right_line + "\n"
        return output