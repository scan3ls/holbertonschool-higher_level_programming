#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    av = dir(hidden_4)
    ac = len(av)
    for i in range(ac):
        if av[i][0] != '_':
            print(av[i])
