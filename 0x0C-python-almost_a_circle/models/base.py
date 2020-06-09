#!/usr/bin/python3
"""Base
"""

import json


class Base:
    """Base class

    Attribute:
        __nb_objects = count of Base objects
    """
    __nb_objects = 0

    @classmethod
    def create(cls, **dictionary):
        """creates instance with all attributes set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if "size" in dictionary:
            cls = Square(1, 0, 0, 0)
            cls.update(
                dictionary['id'],
                dictionary['size'],
                dictionary['x'],
                dictionary['y']
            )
        else:
            cls = Rectangle(1, 1, 0, 0, 0)
            cls.update(
                dictionary['id'],
                dictionary['width'],
                dictionary['height'],
                dictionary['x'],
                dictionary['y']
            )

        return cls

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    def to_json_string(list_dictionaries):
        """returns JSON rep of list_dict"""
        if list_dictionaries is None \
                or list_dictionaries == []:
            return "[]"
        l = []
        for d in list_dictionaries:
            l.append(d.to_dictionary())
        string = json.dumps(l)
        return string

    @staticmethod
    def from_json_string(json_string):
        """convert from json string"""
        if json_string is None\
                or not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """save object to json file"""
        save = cls.to_json_string(list_objs)
        if save == "[]":
            name = "Rectangle"
        else:
            name = type(list_objs[0]).__name__
        with open("{}.json".format(name), 'w') as f:
            f.write(save)

    @classmethod
    def load_from_file(cls):
        """make object/s from json file"""
        filename = cls.__name__ + ".json"

        with open(filename, 'r') as f:
            jsting = f.read()

        list_of_dicts = Base.from_json_string(jsting)
        list_objects = []
        for dictionary in list_of_dicts:
            list_objects.append(Base.create(**dictionary))
        return list_objects
