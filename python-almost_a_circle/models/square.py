#!/usr/bin/python3
"""Square module"""
from symbol import yield_arg
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Return string representation of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
