#!/usr/bin/python3
"""function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts new_string after search_string"""
    with open(filename, 'r', encoding='utf-8') as file_:
        lines = file_.readlines()
    with open(filename, 'w', encoding='utf-8') as file_lines:
        for line in lines:
            file_lines.write(line)
            if search_string in line:
                file_lines.write(new_string + '\n')
