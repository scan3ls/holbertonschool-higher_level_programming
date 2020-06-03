#!/usr/bin/python3
"""Doc"""


class MyList(list):
    """Something
    """

    def __init__(self):
        pass

    def print_sorted(self):
        new_list = self.copy()
        new_list.sort()
        print(new_list)
        del new_list
