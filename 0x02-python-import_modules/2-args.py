#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ar = sys.argv[1:]
    x = 1
    print(f"{len(ar)} arguments:")
    for i in ar:
        print(f"{x}: {i}")
        x += 1
