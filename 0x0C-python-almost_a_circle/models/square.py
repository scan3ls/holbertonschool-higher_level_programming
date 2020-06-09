#!/usr/bin/python3
"""Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        self.int_validator(size, "size", False)
        self.__size = size

        super().__init__(size, size, x, y, id)
        self.__x = x
        self.__y = y

    def __str__(self):
        """string representation"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.__x, self.__y, self.__size)

    @property
    def size(self):
        """ size getter """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter """
        self.int_validator(value, "width")
        if value == 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def update(self, *args, **kwargs):
        """Updates a Rectangle"""

        if args != ():

            attr = {
                0: self.id,
                1: self.__size,
                2: self.__x,
                3: self.__y
            }

            for count, value in enumerate(args):
                attr[count] = value

            self.id, self.__size, self.__x, self.__y = \
                attr[0], attr[1], attr[2], attr[3]

            super().update(attr[0], attr[1], attr[1], attr[2], attr[3])

        else:
            attr = {
                'id': self.id,
                'size': self.__size,
                'x': self.__x,
                'y': self.__y
            }

            for key in kwargs:
                if key in attr:
                    attr[key] = kwargs[key]
            self.id, self.__size, self.__x, self.__y = \
                attr['id'], attr['size'], attr['x'], attr['y']

            super().update(
                attr['id'],
                attr['size'],
                attr['size'],
                attr['x'],
                attr['y']
            )

    def to_dictionary(self):
        """ returns object attributes
            as a dicitionary
        """
        d = {
            'id': self.id,
            'size': self.__size,
            'x': self.__x,
            'y': self.__y
        }

        return d
