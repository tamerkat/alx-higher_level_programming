#!/usr/bin/python3
output = ''.join(chr(i).lower() if i % 2 == 0 else chr(i).upper() for i in range(122, 64, -1))
print(output, end='')
