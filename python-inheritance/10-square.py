#!/usr/bin/python3
"""
Write a Rectangle class that inherits from BaseGeometry
"""
SQ = __import__('8-rectangle').Rectangle


class Square(SQ):
    """Square"""

    def __init__(self, size):
        """init"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__.area(size, size)

    def area(self):
        """Area es area"""
        return super().area()
