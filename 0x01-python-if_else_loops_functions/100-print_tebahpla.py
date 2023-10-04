#!/usr/bin/python3
for t in range(122, 96, -1):
    if t % 2 != 0:
        print("{}".format(chr(t - 32)), end="")
    else:
        print("{}".format(chr(t)), end="")
