#!/usr/bin/python3
for num in range(0, 100):
    if num == 99:
        end = "\n"
    else:
        end = ", "

    print("{num:02d}".format(num=num), end=end)
