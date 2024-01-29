class Square:
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        @property
        def size(self):
            return self.__size
        def size(self, value):
            self.__size = value
    def area(self):
        return self.__size ** 2
