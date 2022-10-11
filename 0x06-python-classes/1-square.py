#!/usr/bin/python3
"""

This module contains a class that defines a square and init method that
sets its size.

"""


class Square():
    """Defines a square."""

    def __init__(self, size):
        """Sets the necessary attributes for the Square object.

        Args:
            size (int): the size of one edge of the square.
        """
        self.__size = size
