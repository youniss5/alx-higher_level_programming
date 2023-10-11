#!/usr/bin/python3
"""class_to_json function"""


def class_to_json(obj):
    """ function that returns the dic description with simple data structure"""
    return obj.__dict__
