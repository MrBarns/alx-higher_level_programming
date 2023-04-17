#!/usr/bin/python3
def fizzbuzz():
    for var in range(1, 101):
        if var % 3 == 0 and var % 5 == 0:
            var = "FizzBuzz"
        elif var % 3 == 0:
            var = "Fizz"
        elif var % 5 == 0:
            var = "Buzz"

        print("{}".format(var), end=" ")
