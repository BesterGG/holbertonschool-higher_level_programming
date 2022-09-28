#!/usr/bin/python3
"""
Write an empty class BaseGeometry
"""


from logging import exception


class BaseGeometry:
    """BG"""
    def area(self):
        raise Exception("area() is not implemented")
