#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
if __name__ == "__main__":

    sq = Square(5)

    print(sq.area())
    print(sq)
    print(sq.size)
    sq.display()

    sq.update(89, 3)
    print()

    print(sq.area())
    print(sq)
    print(sq.size)
    sq.display()

    sq.update(size=4, y=5, x=3)
    print()

    print(sq.area())
    print(sq)
    print(sq.size)
    sq.display()