#!/usr/bin/python3
"""define class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """"define class"""
    def __init__(self, size):
        size.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
        
    def area(self):
        return self.__size ** 2
