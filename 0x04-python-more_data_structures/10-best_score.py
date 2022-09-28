#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_value = 0
    for i in a_dictionary:
        if a_dictionary[i] > best_value:
            best_value = a_dictionary[i]
            best_score = i
        else: continue
    return best_score
