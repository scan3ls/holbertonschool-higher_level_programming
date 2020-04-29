#!/usr/bin/python3
for tens in range(9):
    for ones in range(tens, 10):
        if tens == ones:
            continue
        if tens == 8:
            print("{}{}".format(tens, ones))
        else:
            print("{}{}".format(tens, ones), end=", ")
