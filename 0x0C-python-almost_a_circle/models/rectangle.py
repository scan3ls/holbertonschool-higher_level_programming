#!/usr/bin/python3
"""Rectangle"""

from models.base import Base


class Rectangle(Base):
    """defines a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        is_Pos = True
        is_Not_Pos = False

        self.id = Base(id).id

        self.int_validator(width, "width", is_Not_Pos)
        self.__width = width

        self.int_validator(height, "height", is_Not_Pos)
        self.__height = height

        self.int_validator(x, "x", is_Pos)
        self.__x = x

        self.int_validator(y, "y", is_Pos)
        self.__y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        self.int_validator(value, "width", False)
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        self.int_validator(value, "height", False)
        self.__height = value

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        self.int_validator(value, "x", True)
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        self.int_validator(value, "y", True)
        self.__y = value

    def int_validator(self, value, name, isPos):
        """check value of attributes
            Args:
                isPos: boolen - is x or y posisition attributes
        """

        if type(value) is not int:
            raise TypeError(
                "{} must be an integer"
                .format(name))

        if value <= 0:
            if isPos:
                # Do nothing if a posAttr is 0
                if value != 0:
                    raise ValueError(
                        "{} must be >= 0"
                        .format(name))

            else:
                raise ValueError(
                    "{} must be > 0"
                    .format(name))

    def area(self):
        """Calcs area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """print rectangle to stdout using "#" """

        width, height = self.__width, self.__height
        x, y = self.__x, self.__y

        stdout = ""

        for i in range(y):
            stdout += "\n"
        for row in range(height):
            stdout += (" " * x) + ("#" * width) + "\n"

        print(stdout, end="")
        return stdout

    def __str__(self):
        """ __str__ override """
        string = "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
        return string

    def update(self, *args, **kwargs):
        """Updates a Rectangle"""

        if args != ():
            attr = {
                0: self.id,
                1: self.__width,
                2: self.__height,
                3: self.__x,
                4: self.__y
                }

            for count, value in enumerate(args):
                attr[count] = value

            self.id, self.__width, self.__height, self.__x, self.__y = \
                attr[0], attr[1], attr[2], attr[3], attr[4]
        else:
            attr = {
                'id': self.id,
                'width': self.__width,
                'height': self.__height,
                'x': self.__x,
                'y': self.__y
            }

            for key in kwargs:
                if key in attr:
                    attr[key] = kwargs[key]
            self.id, self.__width, self.__height, self.__x, self.__y = \
                attr['id'], attr['width'], attr['height'], attr['x'], attr['y']

    def to_dictionary(self):
        """ returns object attributes
            as a dictionary
        """
        d = {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }

        return d
