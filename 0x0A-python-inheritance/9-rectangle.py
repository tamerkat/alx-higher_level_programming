#!/usr/bin/python3
"""define class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """function"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def are(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(str(self.__width), str(self.__height)))
