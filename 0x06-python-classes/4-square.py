class Square:
    """ class Square"""


    def __init__(self, size=0):
        """define a square"""
        self.__size = size

        @property
        def size(self):
            return self.__size
        
        @size.setter
        def size(self, value):
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
    def area(self):
        return self.__size ** 2
