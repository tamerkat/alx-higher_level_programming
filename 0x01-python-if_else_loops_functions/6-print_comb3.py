#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if i < j:
            print("{}{}".format(i, j), end="\n" if j == 9 and i == 8 else ", ")
