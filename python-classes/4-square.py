#!/usr/bin/python3
"""
nooo
"""


class Square:
    """
    class
    """

    def __init__(self, size=0):
        """
        thiss
        """
        self.size = size

    @property
    def size(self):
        """
        no
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        calculation
        """
        return self.__size ** 2

    def my_print(self):
        """
        kvadrat olmuytan kvadrat
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
