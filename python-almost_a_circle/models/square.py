#!/usr/bin/python3
"""Square module"""
from symbol import yield_arg
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set size of the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size <= 0:
            raise ValueError("size must be > 0")
        else:
            self.__size = size

    def __str__(self):
        """Return string representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
