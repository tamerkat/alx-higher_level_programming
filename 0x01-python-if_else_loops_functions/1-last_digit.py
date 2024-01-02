#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
positive = number % 10 if number > 0 else number % -10
    
print(
    "Last digit of {:d} is {:d} and is "
    .format(number, positive), end='')
if positive > 5:
    print("greater than 5")
elif positive == 0:
    print("0")
else:
    print("less than 6 and not 0")
