#!/usr/bin/python3
def safe_print_division(a, b):
    if (int(a), int(b)):
        try:
            result = int(a) / int(b)
        except ZeroDivisionError:
            None
        finally:
            print("Inside result: {:d}".format(result))
