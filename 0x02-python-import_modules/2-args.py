#!/usr/bin/python3
def print_args():
    '''
    prints the number of and list of its arguments
    '''
    from sys import argv
    n = len(argv)
    if n == 1:
        print("0 arguments.")
    else:
        if n == 2:
            print("{:d} argument:".format(n - 1))
        else:
            print("{:d} arguments:".format(n - 1))
        for i in range(1, n):
            print("{:d}: {}".format(i, argv[i]))


if __name__ == "__main__":
    print_args()
