#!/usr/bin/python3
def remove_char_at(str, n):
    if 0 > n >= len(str):
        print(str)
    else:
        print(str[:n] + str[n+1:])
