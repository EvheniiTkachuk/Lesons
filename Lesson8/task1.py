def oops(list1):
    for i in range(0, len(list1) + 1):
        print(list1[i])


def oops(dict1):
    print(dict1[0])


list1 = [1, 2, 3, 4]
try:
    oops(list1)
except IndexError:
    print('IndexError')


dict1 = {1: 'one', 2: 'two', 3: 'three'}
try:
    oops(dict1)
except KeyError:
    print('KeyError')
try:
    oops(dict1)
except IndexError:
    print('IndexError')
