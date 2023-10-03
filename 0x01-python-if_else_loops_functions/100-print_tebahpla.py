#!/usr/bin/python3

for code in range(122, 64, -1):

    if 97 <= code <= 122:
        print('{}'.format(chr(code)), end='')
        code = code - 33

    if 65 <= code <= 90:
        print('{}'.format(chr(code)), end='')
        code = code + 31
