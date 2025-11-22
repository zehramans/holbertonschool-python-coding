#!/usr/bin/python3
"""
Is it okay if i add random stuff here
"""


class Square:
    """
    and here
    """

    def __init__(self, size):
        """
        and here
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        again i wasas told to go wild
        """
        return self.__size ** 2
