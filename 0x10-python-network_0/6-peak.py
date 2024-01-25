#!/usr/bin/python3
"""this file contains a function"""


def find_peak(list_of_integers):
    """a function that finds a peak in a list of unsorted integers."""
    if list_of_integers:
        max = 0
        for i in range(0, len(list_of_integers)):
            if list_of_integers[i] > max:
                max = list_of_integers[i]
                i += 1

        return max
    else:
        return None
