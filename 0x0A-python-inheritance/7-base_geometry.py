#!/usr/bin/python3
"""BaseGeometry class module"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """area method"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """method to validate the value"""
        if type(value) != int:
            raise TypeError('<name> must be an integer'.format(name))
        if value <= 0:
            raise ValueError('<name> must be greater than 0'.format(name))
