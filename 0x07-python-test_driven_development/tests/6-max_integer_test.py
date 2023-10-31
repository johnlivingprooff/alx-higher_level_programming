#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Text Class for max_integers function"""
    def test_emptyList(self):
        self.assertIsNone(max_integer([]))

    def test_singlElement(self):
        self.assertEqual(max_integer([4]), 4)

    def test_positiveInt(self):
        self.assertEqual(max_integer([1, 2, 5, 8, 10]), 10)

    def test_negativeInt(self):
        self.assertEqual(max_integer([-1, -10, -5, 0, -45]), 0)
