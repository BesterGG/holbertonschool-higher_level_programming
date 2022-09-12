#!/usr/bin/python3
def max_integer(my_list=[]):
    maxvalue = None
    if not my_list:
        return None
    for num in my_list:
        if maxvalue is None or num > maxvalue:
            maxvalue = num
    return maxvalue
