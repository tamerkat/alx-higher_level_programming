#!/usr/bin/python3
"""class Module"""


class Square:
    """define a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2 or \
                value[0] is not int or value[1] is not int or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        for i in range(self.size):
            print("#" * self.size)
        if not self.size:
            print()
