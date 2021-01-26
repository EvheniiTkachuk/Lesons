# Create your own implementation of an iterable, which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.


def in_range(stop, start=0,  step=1):
    if start != 0:
        stop, start = start, stop
    if start <= stop:
        while start <= stop:
            yield start
            start += step
    else:
        while start >= stop:
            yield start
            start += step


print(f'in_range(5):')
for i in in_range(5):
    print(i, end=' ')


print(f'\n\nin_range(3, 11, 2):')
for i in in_range(3, 11, 2):
    print(i, end=' ')


print(f'\n\nin_range(10, -10, -2):')
for i in in_range(10, -10, -2):
    print(i, end=' ')


