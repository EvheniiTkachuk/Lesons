# Extend the Stack to include a method called get_from_stack that searches and returns
# an element e from a stack. Any other element must remain on the stack respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message


class MyStack:

    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def pop(self):
        return self.array.pop(self.count() - 1)

    def peek(self):
        return self.__current()

    def __current(self):
        return self.array[self.count() - 1]

    def count(self):
        return len(self.array)

    def __iter__(self):
        self.index = self.count() - 1
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration()
        result = self.array[self.index]
        self.index -= 1
        return result

    def get_from_stack(self, item):
        try:
            return self.array.pop(self.array.index(item))
        except (ValueError, TypeError):
            print(f'\nItem "{item}" don\'t found')


if __name__ == "__main__":
    string = '123456789'
    stack = MyStack()

    for i in string:
        stack.push(i)

    for i in stack:
        print(i, end=' ')

    stack.get_from_stack('9')
    stack.get_from_stack('8')
    stack.get_from_stack('7')

    print()
    for i in stack:
        print(i, end=' ')

    stack.get_from_stack('5')
    stack.get_from_stack('4')
    stack.get_from_stack('3')
    stack.get_from_stack('2')

    print()
    for i in stack:
        print(i, end=' ')


    stack.get_from_stack('test')