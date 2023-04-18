#!/usr/bin/python3
from sys import argv

num_args = len(argv)
ind = 1
if num_args == 2:
    print("1 argument:")

elif num_args == 1:
    print("0 arguments.")

else:
    print("{:d} arguments:".format(num_args - 1))

while ind < num_args:
    print("{:d}: {}".format(ind, argv[ind]))
    ind += 1
