#!/usr/bin/python3
"""
    Square class created
"""


class Square:
    """
        Create a instance size inside square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """ Size init"""
        self.size = size
        self.position = position

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position2):
        if len(position2) != 2 or type(position2) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position2[0] < 0 or position2[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(position2[0], int) or isinstance(position2[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for p in range(self.__position[1]):
            print()
        for i in range(self.size):
            for j in range(self.__position[0]):
                print(end=' ')
            for n in range(self.size):
                print('#', end='')
            print()
