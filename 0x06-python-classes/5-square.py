#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size and i != j else "")
        print()
