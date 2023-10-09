#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if sentence:
        b = sentence[0]
    else:
        b = None
    tup = (a, b)
    return tup
