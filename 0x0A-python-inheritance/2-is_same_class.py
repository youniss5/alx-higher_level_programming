#!/usr/bin/python3
"""is same class method"""


def is_same_class(obj, a_class):
    """unction that returns True if the object is exactly an instance of the specified class ; otherwise False"""
    return type(obj) == a_class
