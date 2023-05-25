#!/usr/bin/python3
"""

Module defines function to print fullnames

"""


def say_my_name(first_name, last_name=""):
    """Function prints fullname

    Args:
        first_name (str): first name argument
        last_name (str, optional): last name argument

    Returns:
        0. Prints the first + last names

    Raises:
        TypeError: if first_name and/or last_name is not a str

    """

    try:
        if not first_name or not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
    except Exception as e:
        raise e
    else:
        print("My name is {} {}".format(first_name, last_name))
