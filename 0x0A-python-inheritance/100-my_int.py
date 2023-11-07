#!/usr/bin/python3
"""Has the class MyInt"""


class MyInt(int):
    """this class inverts operands"""
    def __new__(clas, *args, **args_two):
        """new instance of int class"""
        return super(MyInt, clas).__new__(clas, *args, **args_two)

    def __eq__(self, value):
        return int(self) != value

    def __ne__(self, value):
        return int(self) == value
