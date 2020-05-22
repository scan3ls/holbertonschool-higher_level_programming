#!/usr/bin/python3
"""prints a name
"""


def say_my_name(first_name, last_name=""):
    """prints a name

    Args:
        first_name: first name
        last_name: last name
    """

    msg = "say_my_name() missing 1 required positional argument: 'first_name'"

    if first_name is None:
        raise TypeError(msg)
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
