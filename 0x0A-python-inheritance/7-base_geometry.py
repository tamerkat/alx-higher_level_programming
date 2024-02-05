#!/usr/bin/python3
"""class info"""


class BaseGeometry:
    """define class methods"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.value = value
        self.name = name
        
        if not type(value) == int:
            raise TypeError("f{name} must be an integer")
        if value <= 0:
            raise ValueError("f{name} must be greater than 0")
