#!/usr/bin/python3
"""module contains inherited classes"""


class BaseGeometry:

	def __init__(self):
		pass

	def area(self):
		raise Exception("area() is not implemented")
