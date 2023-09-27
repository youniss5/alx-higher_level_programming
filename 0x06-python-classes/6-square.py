#!/usr/bin/python3
"""Module of a square"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing a square,

        Args: 
            size: size of square
            position: position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """get and set size Property of the square"""

        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ set and get the position of the square"""
        return self.__position
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the previous square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print('')
            return
        
        [print('') for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end='') for y in range(0, self.__position[0])]
            [print('#', end='') for z in range(0, self.__size)]
            print('')

