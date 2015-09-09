from random import randint
from math import ceil
import itertools as it
from sys import stdout

from numpy.random import normal


# noinspection PyNoneFunctionAssignment
def generate_attribute(center_value, spread):
    if spread == 0:
        return center_value
    attribute = normal(center_value, spread)
    # noinspection PyTypeChecker
    # attributes are forced to be integers because we're not monsters
    attribute = int(ceil(attribute))
    # attributes less than 1 are not useful in this context
    min_value = 1
    return max(attribute, min_value)


def simulate_chance(percent_chance_success):
    dice_roll = randint(0, 99)
    return dice_roll < percent_chance_success


def raise_(ex):
    raise ex


def get_trimmed_or_padded_string(value, width):
    padding_needed = max(width - len(value), 0)
    padding = " " * padding_needed
    return value[:width] + padding


def join_multi_line_strings(blocks, cell_width):
    output = ""
    left = blocks[0].splitlines()
    if_missing = " " * cell_width
    for block in blocks[1:]:
        right = block.splitlines()
        line_no = 0
        for left_line, right_line in it.izip_longest(left, right, fillvalue=if_missing):
            while line_no >= len(left):
                left.append(if_missing)
            left[line_no] += right_line
            line_no += 1

    for line in left:
        output += line + "\n"
    return output


def query_yes_no(question):

    """
    Ask a yes/no question via the command line.
    :param question: String containing question statement
    :return: True for yes and False for no
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    prompt = " [y/n] "

    while 1:
        stdout.write(question + prompt)
        choice = raw_input().lower()
        if choice in valid.keys():
            return valid[choice]
        else:
            stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")