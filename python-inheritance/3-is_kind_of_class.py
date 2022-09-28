#!/usr/bin/python3
"""
Task 3 - Write a function that returns True if the
object is an instance of, or if the obj is an
instance of a classs that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class)
