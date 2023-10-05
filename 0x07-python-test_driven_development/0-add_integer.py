#!/usr/bin/python3
"""Add integer method"""


def add_integer(a, b=98):
    """Add 2 numbers
    a: first number
    b: second number = 98 (default)

    Return:
    Sum of 2 numbers
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("test/0-add_integer.txt")
