#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv
    from calculator_1 import add
    from calculator_1 import sub
    from calculator_1 import mul
    from calculator_1 import div

    length = len(argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operators = ['+', '-', '*', '/']
    num1, num2 = int(argv[1]), int(argv[3])
    op = argv[2]

    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    result = operations[op](num1, num2)
    string = "{} {} {} = {}".format(num1, op, num2, result)
    print(string)
