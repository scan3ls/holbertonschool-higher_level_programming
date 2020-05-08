#!/usr/bin/python3
def best_score(a_dictionary):
    d = a_dictionary
    best_score = -128

    if d is None:
        return None
    for key in d:
        if d[key] > best_score:
            best_score = d[key]
            best_key = key
    return best_key
