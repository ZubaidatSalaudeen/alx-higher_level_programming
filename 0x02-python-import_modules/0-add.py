#!/usr/bin/python3
def add_1():
    '''
    imports tge function add from the file indicated below
    and outputs the result 1 + 2 = 3
    '''
    from add_0 import add
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))


if __name__ == "__main__":
    add_1()
