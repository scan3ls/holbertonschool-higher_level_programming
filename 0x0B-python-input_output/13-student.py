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

    def to_json(self, attrs=None):
        """Return JSONy values"""

        if attrs is None:
            return dict(self.__dict__)

        attrs = list(attrs)
        new = {}
        d = dict(self.__dict__)

        for item in attrs:
            if item in d:
                new[item] = d[item]
            return new

    def reload_from_json(self, json):
        """replaces all atrributes of the object with json values"""
        if "first_name" in json:
            self.first_name = json["first_name"]
        if "last_name" in json:
            self.last_name = json["last_name"]
        if "age" in json:
            self.age = json["age"]
