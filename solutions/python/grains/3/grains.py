"""Module for working on rice grains on chessboard riddle.
"""

def square(number):
    """Compute of the number of grains on a chess square with formula: 2^(n-1).

    :param number: int - choosen chess square (between 1 - 64)
    :return: int - grains on that specific square
    """
    if 1 <= number <= 64:
        return 2 ** (number -1)
        
    raise ValueError("square must be between 1 and 64")

    
def total():
    """Total number of grains across all squares on the chessboard.
    See: geometric series, summation of geometric series.

    :return: int - total number of grains
    """
    return 2 ** 64 - 1
