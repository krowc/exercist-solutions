"""This module provides functions for determining the nature of a triangle given its sides.
    A triangle may be equilateral, isosceles, or scalene.
"""

def is_valid(sideA, sideB, sideC):
    """Helper function to check whether the side measures are valid.

    :param sideA, sideB, sideC: int - three side measures for a triangle.
    :return: bool - do the side measures satisfy the constraints. See below:

    :constraints: The sum of any two side lengths must be greater than the third side length.
    """
    non_zero = sideA > 0 and sideB > 0 and sideC > 0 

    return sideA + sideB >= sideC and sideB + sideC >= sideA and sideA + sideC >= sideB and non_zero


def equilateral(sides):
    """Checks whether a triangle, given its side measures qualifies as equilateral.

    :param sides: list - contains the three side measures of the triangle.
    :return: bool - is the triangle equilateral.
    """
    sideA, sideB, sideC = sides # The term for this is unpacking a list.
    
    if not is_valid(sideA, sideB, sideC):
        return False
        
    return sideA == sideB == sideC


def isosceles(sides):
    """Checks whether a triangle, given its side measures qualifies as isosceles.
    
    :param sides: list - contains the three side measures of the triangle.
    :return: bool - is the triangle isosceles.

    :constraints: For this exercise, an isoceles triangle has *at least* two sides of equal length.
    """
    sideA, sideB, sideC = sides
    
    if not is_valid(sideA, sideB, sideC):
        return False

    return sideA == sideB or sideB == sideC or sideC == sideA


def scalene(sides):
    """Checks whether a triangle, given its side measures qualifies as scalene.
    
    :param sides: list - contains the three side measures of the triangle.
    :return: bool - is the triangle scalene.
    """
    sideA, sideB, sideC = sides
    
    if not is_valid(sideA, sideB, sideC):
        return False

    return sideA != sideB and sideB != sideC and sideC != sideA