#!/usr/bin/python3
""" my class"""


class MyInt(int):
    """my int class"""
    def __new__(cls, *args, **kwargs):
        """new instance of class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """eq methos"""
        return int(self) != other

    def __ne__(self, other):
        """ne method"""
        return int(self) == other
