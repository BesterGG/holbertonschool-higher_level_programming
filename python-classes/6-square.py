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
        self.__size = size
        self.__position = position

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
    def position(self, position):
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            return self.__position

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
