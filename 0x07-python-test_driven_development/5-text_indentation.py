#!/usr/bin/python3
"""

Module to indent text at certain characters

"""


def text_indentation(text):
    """Function to indent a text

    Args:
        text (str): Text to be indented

    Raises:
        TypeError: if text is not a string

    """

    if type(text) != str:
        raise TypeError("text must be a string")

    buff = ""
    ind = 0
    while ind < len(text):
        buff += text[ind]
        if text[ind] in [".", "?", ":"]:
            buff = buff.strip() + "\n"
            print(buff)
            buff = ""
        ind += 1
    if len(buff):
        print(buff.strip(), end="")
