#!/usr/bin/python3
def read_file(filename=""):
    with open("UTF8", 'r') as f:
        for line in f:
            print(line.strip())
