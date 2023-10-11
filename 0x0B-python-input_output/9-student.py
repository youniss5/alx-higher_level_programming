#!/usr/bin/python3
""" student class"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """init class of student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns a dict of student class"""
        return self.__dict__
