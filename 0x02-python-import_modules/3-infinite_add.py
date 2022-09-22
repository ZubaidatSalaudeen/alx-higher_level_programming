#!/usr/bin/python3
def add_args():
    '''
    prints the result of the addition of all arguments
    '''
    from sys import argv
    result = 0
    for i in range(1, len(argv)):
        result += int(argv[i])
    print("{:d}".format(result))


if __name__ == "__main__":
    add_args()
