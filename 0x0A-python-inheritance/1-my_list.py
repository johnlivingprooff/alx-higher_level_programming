#!/usr/bin/python3
"""
This is a module ``1-my_list``
"""


class MyList(list):
    """class represents a list"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self.copy()))
