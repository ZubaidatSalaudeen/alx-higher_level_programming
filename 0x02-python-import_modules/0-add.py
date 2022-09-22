#!/usr/bin/python3
def add_1():
    '''
    imports tge function add from the file add_0.py
    prints the result of the addition 1 + 2 = 3
    '''
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
if __name__ == "__main__":
    add_1()
