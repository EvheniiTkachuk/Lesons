# Write a Python program to detect the number of local variables declared in a function.


def foo():
    a = 1
    b = 2
    c = 3


def calc_local_var(f):
    return f.__code__.co_nlocals


print(calc_local_var(foo))