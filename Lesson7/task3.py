# A simple calculator.
# # Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
# as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:
# # the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42


def make_operation(operation, *args):
    res = 0
    if operation is '-':
        for j, i in enumerate(args):
            if j is 0:
                res = i
            else:
                res -= i
    elif operation is '+':
        for i in args:
            res += i
    elif operation is '*':
        res = 1
        for i in args:
            res *= i
    print(f'Result expression [', end='')
    for j, i in enumerate(args):
        if i < 0 and j < len(args) - 1:
            print(f'({i}) {operation} ', end='')
        elif i < 0:
            print(f'({i})', end='')
        elif j < len(args) - 1:
            print(f'{i} {operation} ', end='')
        else:
            print(f'{i}', end='')
    print(f'] = {res}')
    return


make_operation('+', 7, 7, 2)
make_operation('-', 5, 5, -10, -20)
make_operation('*', 7, 6)
