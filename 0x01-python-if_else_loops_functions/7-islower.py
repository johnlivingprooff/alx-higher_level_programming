#!/usr/bin/python3
def islower(c):
    a = ord(c)
    for i in range(97, 123):
        if a == i:
            return True
    return False
