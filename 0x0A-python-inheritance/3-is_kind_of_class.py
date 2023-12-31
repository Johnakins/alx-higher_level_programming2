#!/usr/bin/python3
"""Define the class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if the  object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to match the type of the obj.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
