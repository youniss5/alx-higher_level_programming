#!/usr/bin/python3
"""rectangle class method"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square sub-class"""
    def __init__(self, size):
        """init and constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """square area method"""
        return self.__size ** 2
