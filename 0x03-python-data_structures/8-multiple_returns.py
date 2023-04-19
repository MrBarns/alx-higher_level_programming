#!/usr/bin/python3
def multiple_returns(sentence):
    strlen = len(sentence)
    if strlen:
        return (strlen, sentence[0])
    else:
        return (strlen, None)
