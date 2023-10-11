#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    my = dict(sorted(a_dictionary.items(), key=lambda i: i[1], reverse=True))

    keylarge, value = next(iter(my.items()))
    return keylarge
