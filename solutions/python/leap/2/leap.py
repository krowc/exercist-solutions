def leap_year(year):
    div_by_four = year % 4 == 0
    div_by_hundred = year % 100 == 0
    div_by_four_hundred = year % 400 == 0

    is_leap1 = div_by_four and (not div_by_hundred)
    is_leap2 = div_by_hundred and div_by_four_hundred
    return is_leap1 or is_leap2
    
    
