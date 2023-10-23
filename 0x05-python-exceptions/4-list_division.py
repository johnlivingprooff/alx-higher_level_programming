#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length
    try:
        for i in range(0, list_length):
            result[i] = my_list_1[i] / my_list_2[i]
    except (ZeroDivisionError, ValueError, IndexError):
        print("division by 0")
        print("wrong type")
        print("out of range")
        result.append(0)
    return result
