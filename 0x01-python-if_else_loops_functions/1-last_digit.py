#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "and is greater than 5"
str2 = "and is less than 6 and not 0"
if number < 0:
    number *= -1
if number % 10 == 0:
    print("Last digit of {} is {} and is 0".format(number, (number % 10)))
elif number % 10 > 5:
    print("Last digit of {} is {} {}".format(number, (number % 10), str1))
else:
    print("Last digit of {} is {} {}".format(number, (number % 10), str2))
