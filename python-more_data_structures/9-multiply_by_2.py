#!/usr/bin/python3
# https://stackoverflow.com/questions/27518016/apply-function-on-all-values-of-dictionary
def multi(val):
    v = 0
    v = val*2
    return v


def multiply_by_2(dic1):
    dic2 = {}
    dic2 = {k: multi(v) for k, v in dic1.items()}
    return dic2
