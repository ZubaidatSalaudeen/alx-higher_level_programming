def max_integer(my_list=[]):
    max_int = 0
    for i in my_list:
        if i > max_int:
            max_int = i
        else:
            continue
    return max_int
