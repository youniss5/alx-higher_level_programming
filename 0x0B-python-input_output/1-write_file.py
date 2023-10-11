#!/usr/bin/python3
"""write_file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns the number of chars"""
    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)
