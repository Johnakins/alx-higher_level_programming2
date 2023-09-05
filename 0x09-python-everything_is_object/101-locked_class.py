#!/usr/bin/python3
"""Define the locked class."""


class LockedClass:
    """
    This prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
