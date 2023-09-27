#!/usr/bin/python3
"""Module of a square"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initializing a square,

        Args: size of square

        """
        self.size = size
    @property
    def size(self):
        """Property"""

        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the previous square"""
        return self.__size ** 2
