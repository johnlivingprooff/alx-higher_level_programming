#!/usr/bin/python3
"""this file contains a function"""


def find_peak(list_of_integers):
    """A function that finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None

    peak = 0
    num = len(list_of_integers) - 1

    while peak < num:
        mid = peak + (num - peak) // 2

        if list_of_integers[mid] >= list_of_integers[mid - 1] and \
           list_of_integers[mid] >= list_of_integers[mid + 1]:
            return list_of_integers[mid]

        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            peak = mid + 1
        else:
            num = mid - 1

    return list_of_integers[peak]
