#!/usr/bin/python3
def import_var_a():
    '''
    imports a variable "a" from the file variable_load_5.py and prints its value
    '''
    from variable_load_5 import a
    print(a)
if __name__ == "__main__":
    import_var_a()
