#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv)
    sum = 0
    for i in range(1, ac):
        sum += int(argv[i])
    print(sum)
