#!/usr/bin/python3
"""Recntagle class that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """Recntagle class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        for y in range(self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(self.__x):
                print(" " * self.__x, end="")
            for j in range(0, self.__width):
                print("#", end='')
            print()
        # """Returns the display of the Rectangle"""
        # for i in range(0, self.__height):
        #     for j in range(0, self.__width):
        #         print("#", end='')
        #     print()

    def __str__(self):
        """Returns the string representation of the Rectangle"""
        p = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        p1 = f" - {self.__width}/{self.__height}"
        return p + p1
