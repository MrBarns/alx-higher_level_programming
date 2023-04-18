#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    total = 0
    if len(argv) > 1:
        for num in argv:
            if num != argv[0]:
                total += int(num)

    print(total)
