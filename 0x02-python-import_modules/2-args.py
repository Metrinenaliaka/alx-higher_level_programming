#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv) - 1
    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_count))
    for i in range(arg_count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
