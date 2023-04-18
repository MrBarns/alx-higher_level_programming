#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    # import sys
    from sys import argv, exit as sys_exit

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys_exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    ops = ['+', '-', '*', '/']
    funcs = [add, sub, mul, div]

    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys_exit(1)

    for op, func in zip(ops, funcs):
        if operator == op:
            print("{:d} {} {:d} = {:d}".format(a, operator, b, func(a, b)))

    sys_exit(0)
