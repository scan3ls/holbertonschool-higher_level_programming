#!/usr/bin/python3
""" Test for rectangle.py
"""


import unittest
from models import base, rectangle


class TestRectMethods(unittest.TestCase):
    """rect tests"""

    def test_inherits(self):
        """test if Rectangle inherits from Base"""

        b = base.Base()
        rect = rectangle.Rectangle(1, 1)

        self.assertTrue(issubclass(type(rect), type(b)))

    def test_has_attributes(self):
        """verify has specific attributes with getters and setters"""

        rect = rectangle.Rectangle(1, 1)
        list_of_attr = dir(rect)
        attr = [
            'id',
            '_Rectangle__width',
            '_Rectangle__height',
            '_Rectangle__x',
            '_Rectangle__y'
        ]
        getter_setter = ['height', 'width', 'x', 'y']

        result = True

        for item in attr:
            if item not in list_of_attr:
                print("\t!!!! Not Found: ", item, " !!!!")
                result = False

        for item in getter_setter:
            if item not in list_of_attr:
                print("\t!!!!! Not Found: ", item, " !!!!")
                result = False

        self.assertTrue(result)

    def test_constructor(self):
        """ verify rect has correct attributes set """

        rect = rectangle.Rectangle(5, 3, 7, 2, 99)

        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 7)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.id, 99)

    def test_validator(self):
        """ validate the validation of attributes """

        # width type validation
        with self.assertRaises(TypeError) as cm:
            rectangle.Rectangle('1', 2)

        msg = cm.exception
        self.assertEqual('width must be an integer', str(msg))

        # height type validation
        with self.assertRaises(TypeError) as cm:
            rectangle.Rectangle(1, '2')

        msg = cm.exception
        self.assertEqual('height must be an integer', str(msg))

        # width value validation
        with self.assertRaises(ValueError) as cm:
            rectangle.Rectangle(0, 2)

        msg = cm.exception
        self.assertEqual('width must be > 0', str(msg))

        # height value validation
        with self.assertRaises(ValueError) as cm:
            rectangle.Rectangle(1, -2)

        msg = cm.exception
        self.assertEqual('height must be > 0', str(msg))

        # x value validation
        with self.assertRaises(ValueError) as cm:
            rectangle.Rectangle(1, 1, -1, 1)

        msg = cm.exception
        self.assertEqual('x must be >= 0', str(msg))

        # y value validation
        with self.assertRaises(ValueError) as cm:
            rectangle.Rectangle(1, 1, 1, -1)

        msg = cm.exception
        self.assertEqual('y must be >= 0', str(msg))

    def test_area(self):
        """test area function of Rectangle"""
        rect = rectangle.Rectangle(7, 3)

        dir_list = dir(rect)

        if 'area' in dir_list:
            result = True
        else:
            print("\t!!!! Missing area function !!!!")
            result = False

        self.assertTrue(result)
        self.assertEqual(rect.area(), 21)

    def test_display(self):
        """ test string representation
            to stdout
        """

        rect = rectangle.Rectangle(2, 2)
        target_out = "##\n##\n"
        stdout = rect.display()

        self.assertEqual(stdout, target_out)

    def test_str(self):
        """ test string __str__ override """

        rect = rectangle.Rectangle(1, 1, 0, 0)
        base_id = rect.id

        rect1 = rectangle.Rectangle(4, 6, 2, 1, 7)

        self.assertEqual(
            str(rect1),
            "[Rectangle] (7) 2/1 - 4/6"
        )

        rect2 = rectangle.Rectangle(5, 5, 1)

        self.assertEqual(
            str(rect2),
            "[Rectangle] ({}) 1/0 - 5/5".format(
                base_id + 1
            )
        )

    def test_update_args(self):
        """ verify update success with args """

        rect = rectangle.Rectangle(5, 5)

        # check for function
        self.assertTrue('update' in dir(rect))

        # test id update
        rect.update(89)
        self.assertEqual(rect.id, 89)

        # test width update
        rect.update(89, 2)
        self.assertEqual(rect.width, 2)

        # test height upadte
        rect.update(89, 2, 3)
        self.assertEqual(rect.height, 3)

        # test x update
        rect.update(89, 2, 3, 4)
        self.assertEqual(rect.x, 4)

        # test y update
        rect.update(89, 2, 3, 4, 2)
        self.assertEqual(rect.y, 2)

    def test_update_kwargs(self):
        """ verify update success with kwargs """

        rect = rectangle.Rectangle(1, 1, 0, 0, 1)

        # test id update
        rect.update(id=89)
        self.assertEqual(rect.id, 89)

        # test width update
        rect.update(width=10)
        self.assertEqual(rect.width, 10)

        # test height update
        rect.update(height=10)
        self.assertEqual(rect.height, 10)

        # test x update
        rect.update(x=5)
        self.assertEqual(rect.x, 5)

        # test y update
        rect.update(y=5)
        self.assertEqual(rect.y, 5)

    def test_to_dict(self):
        """ test conversion to dictionary """

        list_of_keys = ['id', 'width', 'height', 'x', 'y']
        result = True

        rect = rectangle.Rectangle(2, 3, 4, 5, 99)
        d = rect.to_dictionary()

        test = {
            'id': 99,
            'width': 2,
            'height': 3,
            'x': 4,
            'y': 5
        }

        for key in list_of_keys:
            if key not in d:
                result = False
                break
            if test[key] != d[key]:
                result = Faslse
                break

        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
