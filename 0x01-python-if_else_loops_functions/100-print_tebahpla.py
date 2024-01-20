#!/usr/bin/python3
for i in range(97, 123, -1):
    if i % 2 == 0:
        print(chr(i).lower(), end='')
    else:
        print(chr(i).upper(), end='')
