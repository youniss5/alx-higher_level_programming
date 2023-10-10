#!/usr/bin/python3
""" rectangle class module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''rectangle sub-class'''
    def __init__(self, width, height):
        '''init and Constructor.'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
