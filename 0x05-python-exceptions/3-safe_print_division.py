#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    if (int(a), int(b)):
        try:
            result = a / b
        except ZeroDivisionError:
            None
        finally:
            print("Inside result: {:d}".format(result))
