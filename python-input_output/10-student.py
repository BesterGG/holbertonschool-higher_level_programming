#!/usr/bin/python3
""" Write a class Student"""


class Student:
    """Student object"""
    def __init__(self, first_name, last_name, age):
        """Initialize the Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a JSON representation of the Student object"""
        list = []
        if attrs is None:
            return self.__dict__
        if type(attrs) is list:
            for i in attrs:
                if hasattr(self, i):
                    list[i] = getattr(self, i)
            return list
