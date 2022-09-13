#!/usr/bin/python3
def search_replace(my_list, search, replace):
    res = list(map(int, list(map(lambda x: str(x).replace(str(search), str(replace)), my_list))))
    return res
