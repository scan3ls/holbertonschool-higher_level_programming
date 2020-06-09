#!/usr/bin/python3
""" Test for square.py
"""


import unittest
from models import base, rectangle, square


class TestSqureMethods(unittest.TestCase):
    """Square tests"""

    def test_inherits(self):
        """ verify square inherits rectangle """

        rect = rectangle.Rectangle(1, 1)
        sqre = square.Square(1)

        self.assertTrue(issubclass(type(sqre), type(rect)))

    def test_has_attributes(self):
        """ verify square has size attribute """

        s = square.Square(1)

        dir_list = dir(s)
        # check for size attribute
        self.assertTrue('_Square__size' in dir_list)

        # TODO: add checks for getter & setter

    def test_constructor(self):
        """ test constructor """
        # TODO: this
        pass

    def test_validator(self):
        """ test integer validation """

        # size type validation
        with self.assertRaises(TypeError) as cm:
            square.Square('1')

        msg = cm.exception
        self.assertEqual('size must be an integer', str(msg))

        # size value validation
        with self.assertRaises(ValueError) as cm:
            square.Square(0)

        msg = cm.exception
        self.assertEqual('size must be > 0', str(msg))

    def test_str(self):
        """ test str overload """

        s = square.Square(1)
        base_id = s.id

        rect1 = square.Square(4, 2, 1, 7)

        self.assertEqual(
            str(rect1),
            "[Square] (7) 2/1 - 4"
        )

        rect2 = square.Square(5, 1)

        self.assertEqual(
            str(rect2),
            "[Square] ({}) 1/0 - 5".format(
                base_id + 1
            )
        )

    def test_area(self):
        """ test for square area """
        # TODO: this
        pass

    def test_display(self):
        """ test for square display """
        # TODO: this
        pass

    def test_update_args(self):
        """ test for square update with args """

        # TODO: this
        pass

    def test_update_kwargs(self):
        """ test for square update with kwargs """

        # TODO: this
        pass

    def test_to_dict(self):
        """ test conversion to dictionary """

        # TODO: this
        pass

if __name__ == '__main__':
    unittest.main()
