#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)
and returns the number of characters written:"""


def write_file(filename="", text=""):
    """opens and writes text to file"""
    with open(filename, "w", encoding="utf-8") as f:
        wrote = f.write(text)
    return wrote
