#!/usr/bin/python3
""" text indentation method"""


def text_indentation(text):
    """function to add new line
    Args:
        string text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")


