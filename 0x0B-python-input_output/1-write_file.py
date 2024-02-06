#!/usr/bin/python3
"""

Reads and prints contents from file
"""


def write_file(filename="", text=""):
    """Read and print text from file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return (f.write(text))
