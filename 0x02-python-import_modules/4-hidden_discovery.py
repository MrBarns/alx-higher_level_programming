#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import re

    for name in dir(hidden_4):
        if not re.search("^_.*", name):
            print(name)
