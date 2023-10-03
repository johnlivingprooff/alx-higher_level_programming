#!/usr/bin/python3
code = 122
while code >= 65:

    if 97 <= code <= 122:
        print('{}'.format(chr(code)), end='')

    code = code - 33

    if 65 <= code <= 90:
        print('{}'.format(chr(code)), end='')

    code = code + 31
