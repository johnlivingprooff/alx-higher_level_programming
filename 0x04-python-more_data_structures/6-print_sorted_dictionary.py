#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorting = dict(sorted(a_dictionary.items()))

    for key, val in sorting.items():
        print('{}: {}'.format(key, val))
