#!/usr/bin/python3
"""Define the class Student."""


class Student:
    """Represent the student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of  student.
            last_name (str): The last name of  student.
            age (int): The age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get dictionary representation of the Student."""
        return self.__dict__
