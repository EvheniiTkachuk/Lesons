# Implement binary search using recursion.


def binary_search_rec(array, item):
    first = 0
    last = len(array) - 1
    midpoint = (first + last) // 2
    if midpoint < 0:
        return False
    if array[midpoint] == item:
        return True
    if item > array[midpoint]:
        return binary_search_rec(array[midpoint + 1:], item)
    return binary_search_rec(array[:midpoint], item)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elem = -5
search = binary_search_rec(lst, elem)
print(f'Find({elem}): {search}')
elem = 1
search = binary_search_rec(lst, elem)
print(f'Find({elem}): {search}')
elem = 5
search = binary_search_rec(lst, elem)
print(f'Find({elem}): {search}')
elem = 10
search = binary_search_rec(lst, elem)
print(f'Find({elem}): {search}')
elem = 15
search = binary_search_rec(lst, elem)
print(f'Find({elem}): {search}')




