#!/usr/bin/python3
""" student class"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """init class of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns a dict of student class and attrs"""
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        this_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                this_dict[key] = value
        return this_dict
