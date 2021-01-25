# Напишите программу Python для доступа к функции внутри функции
# (советы: используйте функцию, которая возвращает другую функцию)


def multiply_10(x):
    return x * 10


def do_twice(f):
    def result_func(x):
        return f(f(x))
    return result_func


res = do_twice(multiply_10)
print(res(5))

print(res.__name__)