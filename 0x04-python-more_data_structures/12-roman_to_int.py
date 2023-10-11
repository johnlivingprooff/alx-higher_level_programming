#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    number, old_val = 0, 0

    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    for i in reversed(roman_string):
        val = roman.get(i, 0)
        if val < old_val:
            number -= val
        else:
            number += val
        old_val = val

    return int(number)
