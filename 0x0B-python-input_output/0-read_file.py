#!/usr/bin/python3
"""this is commit"""


def read_file(filename=""):
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end"")
