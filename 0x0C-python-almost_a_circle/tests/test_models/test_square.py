#!/usr/bin/python3
"""This module contains Test Cases for
models/rectangle.py"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """property evaluation"""
    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_size(self):
        inst = Square(6)

        self.assertEqual(inst.size, 6)
        with self.assertRaises(TypeError):
            Square(4.5)
        with self.assertRaises(ValueError):
            Square(-5)
        with self.assertRaises(TypeError):
            Square(float('inf'))
        with self.assertRaises(TypeError):
            Square(None)

    def test_x_int(self):
        inst = Square(6, 2, 2)

        self.assertEqual(inst.x, 2)
        with self.assertRaises(TypeError):
            Square(5, 4.5)
        with self.assertRaises(ValueError):
            Square(5, -5)
        with self.assertRaises(TypeError):
            Square(5, float('inf'))
        with self.assertRaises(TypeError):
            Square(5, None)

    def test_y_int(self):
        inst = Square(4, 2, 2)

        self.assertEqual(inst.y, 2)
        with self.assertRaises(TypeError):
            Square(5, 4.5)
        with self.assertRaises(ValueError):
            Square(5, -5)
        with self.assertRaises(TypeError):
            Square(5, float('inf'))
        with self.assertRaises(TypeError):
            Square(5, None)


if __name__ == "__main__":
    unittest.main()
