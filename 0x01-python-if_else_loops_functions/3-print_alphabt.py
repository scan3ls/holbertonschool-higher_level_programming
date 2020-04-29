#!/usr/bin/python3
alpha = 97
e = 101
q = 113
for i in range(26):
    if alpha != e and alpha != q:
        print("{:c}".format(alpha), end='')
    alpha += 1
