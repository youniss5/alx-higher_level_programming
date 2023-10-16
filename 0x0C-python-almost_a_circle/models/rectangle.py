#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_int('width', value, False)
        self.__width = value

    @property
    def height(self):
        """rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_int('height', value, False)
        self.__height = value

    @property
    def x(self):
        """ variable"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_int('x', value)
        self.__x = value

    @property
    def y(self):
        """variable"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_int('y', value)
        self.__y = value

    def validate_int(self, name, value, equal=True):
        """validate value method"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if equal and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not equal and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """ the area of rectangle"""
        return self.width * self.height

    def display(self):
        """prints the rectangle"""
        d = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(d, end="")

    def __str__(self):
        """string information of the rectangle"""
        return '[{}] ({}) {}/{} - {}/{}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width,
                   self.height)

     def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''the internal method of rectangle args'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
           if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''the update of rectangle args'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''method to return the dic_ of the rectangle'''
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
