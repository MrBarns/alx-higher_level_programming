#!/usr/bin/python3
uppercase = 0
for ascii_value in range(122, 96, -1):
    if uppercase:
        ascii_value -= 32
        uppercase = 0
    else:
        uppercase = 1

    print("{:c}".format(ascii_value), end="")
