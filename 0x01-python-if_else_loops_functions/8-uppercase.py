#!/usr/bin/python3
def uppercase(str):
    strU = ""
    for char in str:
        i = ord(char)
        if 97 <= i <= 122:
            strU += chr(i - 32)
        else:
            strU += char
    print('{}'.format(strU))
