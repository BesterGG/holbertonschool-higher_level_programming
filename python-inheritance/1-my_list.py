#!/usr/bin/python3
"""
Task 1 - Write a class MyList that inherits from list
"""


class MyList(list):
    """ subclass """
    def print_sorted(self):
        """ print sorted list """
        sl = self.copy()
        sl.sort()
        print(sl)
        return sl
