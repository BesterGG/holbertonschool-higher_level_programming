#!/usr/bin/python3
"""
Task 1 - Write a class MyList that inherits from list
"""


class Mylist(list):
    """Class Mylist"""
    def print_sorted(self):
        l = self.copy()
        l.sort()
        print(l)
        return l
