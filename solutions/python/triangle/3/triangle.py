"""This module provides functions for determining the nature of a triangle given its sides.
    A triangle may be equilateral, isosceles, or scalene.
"""

def is_valid(sides):
    """Helper function to check whether the side measures are valid.

    :param sides: list - three side measures for a triangle.
    :return: bool - do the side measures satisfy the constraints. See below:

    :constraints: The sum of any two side lengths must be greater than the third side length.
    """
    non_zero = sides[0] > 0 and sides[1] > 0 and sides[2] > 0 

    return (sides[0] + sides[1] >= sides[2] and 
            sides[1] + sides[2] >= sides[0] and 
            sides[0] + sides[2] >= sides[1] and 
            non_zero)


def equilateral(sides):
    """Checks whether a triangle, given its side measures qualifies as equilateral.

    :param sides: list - contains the three side measures of the triangle.
    :return: bool - is the triangle equilateral.
    """
    if not is_valid(sides):
        return False
        
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    """Checks whether a triangle, given its side measures qualifies as isosceles.
    
    :param sides: list - contains the three side measures of the triangle.
    :return: bool - is the triangle isosceles.

    :constraints: For this exercise, an isoceles triangle has *at least* two sides of equal length.
    """
    if not is_valid(sides):
        return False

    return sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]


def scalene(sides):
    """Checks whether a triangle, given its side measures qualifies as scalene.
    
    :param sides: list - contains the three side measures of the triangle.
    :return: bool - is the triangle scalene.
    """
    if not is_valid(sides):
        return False

    return sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]