"""Dummy doctring to make linter happy :>"""

def is_armstrong_number(number):
    """Checks if a number is an armstrong number.

    :param number: int - number to be checked.
    :return: bool - is the number an armstrong number.
    """
    num_of_digits = len(str(number))

    total = 0
    for digit in str(number):
        total += int(digit) ** num_of_digits

    return total == number