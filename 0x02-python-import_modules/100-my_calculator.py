#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = sys.argv[1]
    b = sys.argv[3]
    oberation = sys.argv[2]
    if oberation == "+":
        print("{} {} {} = {}".format(a, oberation, b, add(a, b)))
        exit(0)
    elif oberation == "-":
        print("{} {} {} = {}".format(a, oberation, b, sub(a, b)))
        exit(0)
    elif oberation == "*":
        print("{} {} {} = {}".format(a, oberation, b, mul(a, b)))
        exit(0)
    elif oberation == "/":
        print("{} {} {} = {}".format(a, oberation, b, div(a, b)))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
