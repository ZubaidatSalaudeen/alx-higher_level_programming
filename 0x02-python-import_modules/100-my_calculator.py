#!/usr/bin/python3
def my_calculator():
    '''
    imports funcgions fom the file indicated below
    and handles basic operations
    '''
    from calculator_1 import add, sub, mul, div
    from sys import argv
    n = len(argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if argv[2] == "+":
            result = add(int(argv[1]), int(argv[3]))
        elif argv[2] == "-":
            result = sub(int(argv[1]), int(argv[3]))
        elif argv[2] == "*":
            result = mul(int(argv[1]), int(argv[3]))
        elif argv[2] == "/":
            result = div(int(argv[1]), int(argv[3]))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print("{} {} {} = {:d}".format(argv[1], argv[2], argv[3], result))


if __name__ == "__main__":
    my_calculator()
