#!/usr/bin/python3
def search_replace(my_list, search, replace):
    f = list(map(lambda x: str(x).replace(str(search), str(replace)), my_list))
    res2 = list(map(int, f))
    return res2
