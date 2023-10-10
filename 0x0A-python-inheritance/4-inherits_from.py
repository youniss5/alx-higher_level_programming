#!/usr/bin/python3
"""method of inherits_from"""


def inherits_from(obj, a_class):
    """check if object is a subclass"""
    return isinstance(obj, a_class) and type(obj) != a_class
