"""
jar.py - Cookie Jar Implementation

Author: TJ Tryon
Date: August 01, 2025

Usage: from jar import Jar
Example: jar = Jar(10); jar.deposit(3); print(jar)

This module implements a cookie jar class that can store a limited number
of cookies. Provides methods to deposit and withdraw cookies with proper
capacity validation and error handling.
Uses cookie emoji (🍪) for visual representation.
"""


class Jar:
    """
    A cookie jar that can store cookies up to a specified capacity.

    Provides methods to deposit and withdraw cookies with validation
    to ensure capacity limits and available cookies are respected.
    """

    def __init__(self, capacity=12):
        """
        Initialize a cookie jar with the given capacity.

        Args:
            capacity (int): Maximum number of cookies the jar can hold (default: 12)

        Raises:
            ValueError: If capacity is not a non-negative integer
        """
        # Validate that capacity is a non-negative integer
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")

        # Set the jar's capacity and initialize with no cookies
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        """
        Return string representation of the cookie jar.

        Returns:
            str: Cookie emoji (🍪) repeated for each cookie in the jar
        """
        return "🍪" * self._size

    def deposit(self, n):
        """
        Add n cookies to the cookie jar.

        Args:
            n (int): Number of cookies to add

        Raises:
            ValueError: If adding n cookies would exceed the jar's capacity
        """
        # Check if adding n cookies would exceed capacity
        if self._size + n > self._capacity:
            raise ValueError("Cannot deposit: would exceed jar capacity")

        # Add the cookies to the jar
        self._size += n

    def withdraw(self, n):
        """
        Remove n cookies from the cookie jar.

        Args:
            n (int): Number of cookies to remove

        Raises:
            ValueError: If there aren't enough cookies in the jar to withdraw
        """
        # Check if there are enough cookies to withdraw
        if n > self._size:
            raise ValueError("Cannot withdraw: not enough cookies in jar")

        # Remove the cookies from the jar
        self._size -= n

    @property
    def capacity(self):
        """
        Return the cookie jar's capacity.

        Returns:
            int: Maximum number of cookies the jar can hold
        """
        return self._capacity

    @property
    def size(self):
        """
        Return the number of cookies currently in the jar.

        Returns:
            int: Current number of cookies in the jar
        """
        return self._size
