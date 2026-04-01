"""This module provides functions for determining the nature of a triangle given its sides.
    A triangle may be equilateral, isosceles, or scalene.
"""
def is_valid(a, b, c):
    """Helper function to check whether the side measures are valid.

    :param a, b, c: int - three side measures for a triangle.
    :return: bool - do the side measures satisfy the constraints. See below:

    :constraints: The sum of any two side lengths must be greater than the third side length.
    """
    non_zero = a > 0 and b > 0 and c > 0 
    return a + b >= c and b + c >= a and a + c >= b and non_zero


def equilateral(sides):
    """Checks whether a triangle, given its side measures qualifies as equilateral.

    :param sides: list - contains the three side measures of the triangle.
    :return: bool - is the triangle equilateral.
    """
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    if not is_valid(a, b, c):
        return False
        
    return a == b and b == c and c == a


def isosceles(sides):
    """Checks whether a triangle, given irs side measures qualifies as scalene.
    
    :param sides: list - contains the three side measures of the triangle.
    :return: bool - is the triangle isosceles.

    :constraints: For this exercise, an isoceles triangle has *at least* two sides of equal length.
    """
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    if not is_valid(a, b, c):
        return False

    return a == b or b == c or c == a

def scalene(sides):
    """Checks whether a triangle, given irs side measures qualifies as isosceles.
    
    :param sides: list - contains the three side measures of the triangle.
    :return: bool - is the triangle scalene.
    """
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    if not is_valid(a, b, c):
        return False

    return a != b and b != c and c != a
