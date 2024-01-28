#!/usr/bin/python3
""" square module"""


class Square:
    """define square function"""
    def __init__(self, size=0):
        self.__size = size
        try:
            size = int(size)
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
