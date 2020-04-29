#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

str0 = "Last digit of"
str1 = "and is greater than 5"
str2 = "and is 0"
str3 = "and is less than 6 and not 0"

if number < 0:
    number *= -1
    rem = number % 10
    number *= -1
    rem *= -1
    if rem == 0:
        print("{} {} is {} {}".format(str0, number, rem, str2))
    else:
        print("{} {} is {} {}".format(str0, number, rem, str3))
else:
    rem = number % 10
    if rem == 0:
        print("{} {} is {} {}".format(str0, number, rem, str2))
    elif rem < 6:
        print("{} {} is {} {}".format(str0, number, rem, str3))
    else:
        print("{} {} is {} {}".format(str0, number, rem, str1))
