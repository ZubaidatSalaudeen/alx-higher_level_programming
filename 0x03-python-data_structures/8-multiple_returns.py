#!/usr/bin/python3
def multiple_returns(sentence):
    sen_tuple = tuple(sentence)
    if sentence == "":
        return (len(sen_tuple), None)
    return (len(sen_tuple), sen_tuple[0])
