#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    maxi = my_list[0]

    for x in my_list:
        if x > maxi:
            maxi = x

    return maxi
