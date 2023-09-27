#!/usr/bin/python3
"""Module of a square"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """Initializing a square,

        Args: size of square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
