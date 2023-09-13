#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxvalue = 0
    maxk = None
    for key, v in a_dictionary.items():
        if v > maxvalue:
            maxvalue = v
            maxk = key
    return maxk
