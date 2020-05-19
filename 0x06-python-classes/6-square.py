#!/usr/bin/python3
class Square:
    """makes a square"""
    def __init__(self, size=0, position=(0, 0)):
        """init function"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """position property"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """find area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """print square with #"""
        size = self.__size
        ypos = self.__position[1]
        xpos = self.__position[0]

        if size == 0:
            print()
        for line in range(ypos):
            print()

        for y in range(size):
            for space in range(xpos):
                print(" ", end="")
            for x in range(size):
                print("#", end="")
            print()
