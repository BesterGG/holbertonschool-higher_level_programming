#!/usr/bin/python3
"""
Task 2 - Write a function that returns True if the
object is exactly an instance of the specified class
Otherwise False
"""


def is_same_class(obj, a_class):
    """Function which returns true if the object is
    exactly an instance of the class"""
    return type(obj) is a_class
