def is_armstrong_number(number):
    num_of_digits = len(str(number))

    sum = 0
    for index, digit in enumerate(str(number)):
        sum += int(digit) ** num_of_digits

    return sum == number

