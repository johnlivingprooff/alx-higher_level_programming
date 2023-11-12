#!/usr/bin/python3
"""This module contains Test Cases for
models/rectangle.py"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """property evaluation"""
    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_width(self):
        inst = Rectangle(4, 6)

        self.assertEqual(inst.height, 6)
        with self.assertRaises(TypeError):
            Rectangle(4.5, 6)
        with self.assertRaises(ValueError):
            Rectangle(-5, 6)
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 5)

    def test_height(self):
        inst = Rectangle(4, 6)

        self.assertEqual(inst.height, 6)
        with self.assertRaises(TypeError):
            Rectangle(6, 4.5)
        with self.assertRaises(ValueError):
            Rectangle(6, -5)
        with self.assertRaises(TypeError):
            Rectangle(4, float('inf'))

    def test_x_int(self):
        inst = Rectangle(4, 6, 2, 2)

        self.assertEqual(inst.x, 2)

    def test_y_int(self):
        inst = Rectangle(4, 6, 2, 2)

        self.assertEqual(inst.y, 2)


if __name__ == "__main__":
    unittest.main()
