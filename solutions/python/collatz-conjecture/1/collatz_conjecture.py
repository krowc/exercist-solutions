"""Dummy docstring for Collatz Conjecture.

idea: if x % 2 == 0; x = x / 2
      if x % 2 != 0; x = 3x + 1

repeat until x = 1
"""

def steps(number):
    """Counts how many steps it takes to reach 1 according to the rules of the 
    Collatz Conjecture.

    :param number: int - number to subject to the conjecture.
    :return: int - number of steps it took to reach 1.
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    count = 0
    while number != 1:
        if number % 2 == 0:
            number /= 2
            count += 1

        else:
            number = 3*number + 1
            count += 1

    return count