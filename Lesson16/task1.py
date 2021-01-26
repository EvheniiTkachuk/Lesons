# Create your own implementation of a built-in function enumerate,
# named `with_index`, which takes two parameters: `iterable` and `start`,
# default is 0. Tips: see the documentation for the enumerate function


def with_index(iterable, index=0):
    for j in iterable:
        yield j, index
        index += 1


my_list = ['a', 'b', 'c', 'd', 'e', 'f']
gen = with_index(my_list)

print(type(gen))

for i in gen:
    print(i)


gen = with_index(my_list, 100)

for value, i in gen:
    print(f'index: {i}, value: {value}')

