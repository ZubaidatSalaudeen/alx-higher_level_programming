#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    '''
    Adds 2 tuples
    Returns a tuple with 2 integers:
    tuple_ab_0 : The addition of the first element of each argument
    tuple_ab_2: The addition of the second element of each integer
    '''
    if len(tuple_a) < 2:
        tuple_a += (0, 0)
    if len(tuple_b) < 2:
        tuple_b += (0, 0)
    tuple_ab_0 = tuple_a[0] + tuple_b[0]
    tuple_ab_1 = tuple_a[1] + tuple_b[1]
    return (tuple_ab_0, tuple_ab_1)
