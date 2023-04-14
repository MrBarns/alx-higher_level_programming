#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = ((number * -1) % 10) * -1
else:
    digit = (number % 10)

if digit > 5:
    print(
        f"The last digit of {number:d} is {digit:d} and is greater than 5"
    )
elif digit == 0:
    print(f"The last digit of {number:d} is {digit:d} and is 0")
else:
    print(
        f"The last digit of {number:d} is\
 {digit:d} and is less than 6 and not 0"
    )
