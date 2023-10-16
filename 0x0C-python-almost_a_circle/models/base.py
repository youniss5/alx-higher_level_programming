#!/usr/bin/python3
"""base class module"""


class base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not none:
            self.id = id
        else:
            base.__nb_objects += 1
            self.id =  base.__nb_objects
