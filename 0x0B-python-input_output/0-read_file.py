#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it"""
    with open(filename, "r", encoding='utf-8') as fl:
            print(fl.read(), end="")
