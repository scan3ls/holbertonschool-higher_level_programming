#!/usr/bin/python3
def uppercase(str):
    length = len(str)
    for i in range(length):
        c = ord(str[i])
        print("{:c}".format(c if c < 93 else c - 32), end='')
    print("")
