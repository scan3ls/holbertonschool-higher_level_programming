#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num2 = number
str1 = "and is greater than 5"
str2 = "and is less than 6 and not 0"
if num2 < 0:
    num2 *= -1
if num2 % 10 == 0:
    print("Last digit of {} is {} and is 0".format(number, (num2 % 10)))
elif num2 % 10 > 5:
    print("Last digit of {} is {} {}".format(number, (num2 % 10), str1))
else:
    print("Last digit of {} is {} {}".format(number, (num2 % 10), str2))
