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
    min_value = 1
    # noinspection PyTypeChecker
    attribute = int(ceil(attribute))
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


def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while 1:
        stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return default
        elif choice in valid.keys():
            return valid[choice]
        else:
            stdout.write("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")