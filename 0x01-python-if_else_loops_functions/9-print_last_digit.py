#!/usr/bin/python3
def print_last_digit(number):
    # print_last_digit - returns the value of the last digit of a number
    # number - number to find last digit of

    if number < 0:
        number *= -1
    print("{}".format(number % 10), end='')
    return (number % 10)
