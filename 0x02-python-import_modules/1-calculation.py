#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    ad = add(a, b)
    su = sub(a, b)
    mu = mul(a, b)
    di = div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, ad))
    print("{:d} - {:d} = {:d}".format(a, b, su))
    print("{:d} * {:d} = {:d}".format(a, b, mu))
    print("{:d} / {:d} = {:d}".format(a, b, di))
