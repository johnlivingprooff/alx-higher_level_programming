#!/usr/bin/python3
"""
This module contains a function
that prints a text with 2 new lines
after each of these characters: ., ? and :

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines
    after each of these characters: ., ? and :
    Args: text(str): the text to print
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiter = [':', '?', '.']
    for char in delimiter:
        text = (char + '\n\n').join(
            [row.strip() for row in text.split(char)]
        )
    print(text)
