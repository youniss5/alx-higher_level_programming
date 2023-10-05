#!/usr/bin/python3
"""print square method"""


def print_square(size):
    """print square method to print square with a symbol
    Args:
        size: the size of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print(("#" * size + "\n"), end="")
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
