#!/usr/bin/python3
def common_elements(s1, s2):
    res = []
    for key in s1:
        for key2 in s2:
            if key == key2:
                res.append(key)
    return res
