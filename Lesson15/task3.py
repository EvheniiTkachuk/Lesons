# Write a class TypeDecorators which has several methods for converting results
# of functions to a specified type (if it's possible):

from functools import wraps


class TypeDecorator:

    @staticmethod
    def template(type_: type):
        def decorator(func):
            @wraps(func)
            def wrapper(var):
                try:
                    res = type_(var)
                    return res
                except (TypeError, ValueError):
                    print(f'Cant transform "{var}" to type {type_}')
            return wrapper
        return decorator


@TypeDecorator.template(int)  # to_int
def do_nothing(str_):
    return str_


test = do_nothing("25")
print(f'{test} [{type(test)}]')
test = do_nothing("qwe")
print(f'{test} [{type(test)}]')
print(f'{do_nothing.__name__}\n')


@TypeDecorator.template(float)  # to_float
def do_nothing(str_):
    return str_


test = do_nothing("25")
print(f'{test} [{type(test)}]')
test = do_nothing("qwe")
print(f'{test} [{type(test)}]')
print(f'{do_nothing.__name__}\n')


@TypeDecorator.template(bool)  # to_bool
def do_nothing(str_):
    return str_


test = do_nothing("25")
print(f'{test} [{type(test)}]')
test = do_nothing("qwe")
print(f'{test} [{type(test)}]')
print(f'{do_nothing.__name__}\n')


@TypeDecorator.template(str)  # to_str
def do_nothing(str_):
    return str_


test = do_nothing("25")
print(f'{test} [{type(test)}]')
test = do_nothing("qwe")
print(f'{test} [{type(test)}]')
print(f'{do_nothing.__name__}\n')
