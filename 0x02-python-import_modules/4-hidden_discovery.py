#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    result = dir(hidden_4)
    for i in result:
        if i[:2] != "__":
            print(i)

