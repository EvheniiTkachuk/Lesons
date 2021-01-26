from functools import wraps


def arg_rules(type_: type, max_length: int, contains: list) -> (bool, str):
    def decorator(func):
        @wraps(func)
        def wrapper(name):
            if all([type_ == type(name), max_length >= len(name),
                    all([bool(name.count(res)) for res in contains])]):
                return func(name)
            else:
                return False
        return wrapper
    return decorator


@arg_rules(str, 15, ['05', '@'])
def create_slogan(name):
    return f'{name} пьет пепси в своем новеньком BMW!'


print(f'1. assert "Steve":\t{create_slogan("Steve")}')
print(f'2. assert "johndoe05@gmail.com":\t{create_slogan("johndoe05@gmail.com ")}')
print(f'3. assert "S @ SH05":\t{create_slogan("S @ SH05")}')
