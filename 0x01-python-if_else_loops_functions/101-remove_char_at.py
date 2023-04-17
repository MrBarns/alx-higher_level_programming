#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = ""
    for index in range(0, len(str)):
        if index != n:
            strcpy += str[index]

    return strcpy
