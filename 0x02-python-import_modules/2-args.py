#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ar = sys.argv[1:]
    x = 1
    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 arguments:")
    else:
        print(f"{len(ar)} arguments")
        for i in ar:
            print(f"{x}: {i}")
            x += 1
