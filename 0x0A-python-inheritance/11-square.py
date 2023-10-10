#!/usr/bin/python3
"""rectangle class module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """rectangle sub class"""
    def __init__(self, size):
        """init and  constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ square area method"""
        return self.__size ** 2

    def __str__(self):
        """return the string of square"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
