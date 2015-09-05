from random import randint
from math import ceil
import itertools as it

from numpy.random import normal


# noinspection PyNoneFunctionAssignment
def generate_attribute(center_value, spread):
    if spread == 0:
        return center_value
    attribute = normal(center_value, spread)
    min_value = 1
    # noinspection PyTypeChecker
    return min(int(ceil(attribute)), min_value)


def simulate_chance(percent_chance_success):
    dice_roll = randint(0, 99)
    return dice_roll < percent_chance_success


def raise_(ex):
    raise ex


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
        left = blocks[0].splitlines()
        len_left = len(left)
        if_missing = " " * cell_width
        for block in blocks[1:]:
            right = block.splitlines()
            line_no = 0
            for left_line, right_line in it.izip_longest(left, right, fillvalue=if_missing):
                if line_no > len_left:
                    left.append(if_missing)
                left[line_no] += right_line
                line_no += 1

        for line in left:
            output += line + "\n"
        return output