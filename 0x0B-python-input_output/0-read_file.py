#!/usr/bin/python3
"""this is commit"""


def read_file(filename=""):
    """ define"""
    with open(filename, mode='r', encoding='utf-8') as f:
        print(f.read(), end"")
