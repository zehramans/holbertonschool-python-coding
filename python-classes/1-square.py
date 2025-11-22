#!/usr/bin/python3"
"""
Is it okay if i add random stuff here
"""


class Square:
    """
    and here
    """

    def __init__(self, size=0):
        """
        and here
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
