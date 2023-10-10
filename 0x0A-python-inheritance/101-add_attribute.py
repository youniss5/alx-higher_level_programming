#!/usr/bin/python3
"""function that add attribute to an object"""


def add_attribute(obj, att, value):
    """Add new attribute"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
