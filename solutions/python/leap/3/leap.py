def leap_year(year):
    """A function that determines whether the given year is a leap year or not.

    :param year: int - year in question.    
    :return: bool - is the year in question a leap year or not.
    """
    div_by_four = year % 4 == 0
    div_by_hundred = year % 100 == 0
    div_by_four_hundred = year % 400 == 0

    is_leap = (div_by_four and not div_by_hundred) or (div_by_hundred and div_by_four_hundred)

    return is_leap
    
