def uppercase(str):
    # uppercase - prints a string in uppercase followed by a newline
    # str: string to print
    length = len(str)
    for i in range(length):
        c = ord(str[i])
        print("{:c}".format(c if c < 93 else c - 32), end='')
    print("")
