#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test function max_integer"""
    def test_values(self):
        """Test with lists containing real numbers"""
        l1 = [0, 1, 2, 3, 4, 5]
        l2 = [-1, -2, -3, -4, -5]
        l3 = []

        self.assertAlmostEqual(max_integer(l1), 5)
        self.assertAlmostEqual(max_integer(l2), -1)
        self.assertAlmostEqual(max_integer(l3), None)

    def test_types(self):
        """Test if list contains differing types"""
        l1 = [0, 1, 2, '3', 4, 5]
        l2 = [-1, -2, "three", -4, -5]

        self.assertRaises(TypeError, max_integer, l1)
        self.assertRaises(TypeError, max_integer, l2)
