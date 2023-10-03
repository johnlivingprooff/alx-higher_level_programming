#!/usr/bin/python3
def pow(a, b):
    if b >= 0:
        res = 1
        while b > 0:
            res *= a
            b -= 1
    else:
        res = 1 / pow(a, -b)
    return res
