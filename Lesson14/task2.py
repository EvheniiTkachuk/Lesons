from functools import wraps


def stop_words(words_list):
    def decorator(func):
        @wraps(func)
        def wrapper(name):
            s = func(name)
            for word in words_list:
                s = s.replace(word, '***')
            return s
        return wrapper
    return decorator


words = ['пепси', 'BMW']


@stop_words(words)
def create_slogan(name):
    return f'{name} пьет пепси в своем новеньком BMW!'


print(create_slogan('Стив'))


