#!/usr/bin/python3
"""Defines the object attribute lookup function."""


def lookup(obj):
    """Return the list of the object's available attributes."""
    return (dir(obj))
