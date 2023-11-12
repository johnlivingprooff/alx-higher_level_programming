#!/usr/bin/python3
"""This module contains Test Cases for
Project Almost a Circle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """property evaluation"""
    def test_width_is_int(self):
        inst = Rectangle(4, 6)

        self.assertEqual(inst.width, 4)

        with self.assertRaises(ValueError):
            Rectangle(4.5, 8)

    def test_height_is_int(self):
        inst = Rectangle(4, 6)

        self.assertEqual(inst.height, 6)

    def test_x_int(self):
        inst = Rectangle(4, 6, 2, 2)

        self.assertEqual(inst.x, 2)

    def test_y_int(self):
        inst = Rectangle(4, 6, 2, 2)

        self.assertEqual(inst.y, 2)


if __name__ == "__main__":
    unittest.main()
