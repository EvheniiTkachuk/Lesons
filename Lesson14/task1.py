# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!

from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args):
        print(f'{func.__name__} called with {args}')
    return wrapper


@logger
def add(x, y):
    return x, y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(4, 5)
square_all(1, 2, 3, 4, 5)

print(add.__name__)
print(square_all.__name__)
