#!/usr/bin/python3
"""
This module contains a function that
prints My name is <first name> <last name>
where <first name> and <last name> are
the names of the user
"""


def say_my_name(first_name, last_name=""):
    """this function prints out:
        "My name is <first name> <last name>"
    Args: first_name(str): the <first name>
          last_name(str): default is empty
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
