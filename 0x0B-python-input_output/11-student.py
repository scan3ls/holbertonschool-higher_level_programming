#!/usr/bin/python3
"""Students
"""


class Student:
    """Muh student"""

    def __init__(self, first_name, last_name, age):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return JSONy values"""
        return dict(self.__dict__)
