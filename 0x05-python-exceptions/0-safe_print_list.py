#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for x in range(0, x):
            print(my_list[x], end="")
            count += 1
    except Exception:
        pass
    print()
    return count
