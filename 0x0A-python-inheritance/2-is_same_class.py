#!/usr/bin/python3
"""Define the class-checking function."""


def is_same_class(obj, a_class):
    """Check if the object isan  instance of a given class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to match the type of the obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
