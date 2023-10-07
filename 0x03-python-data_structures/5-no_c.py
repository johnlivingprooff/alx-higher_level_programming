#!/usr/bin/python3
def no_c(my_string):
    edited = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            edited += i
    return edited
