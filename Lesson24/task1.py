# Write a program that reads in a sequence of characters and prints
# them in reverse order, using your implementation of Stack.


class MyStack:

    def __init__(self):
        self.array = []

    def push(self, item):
        self.array.append(item)

    def pop(self):
        return self.array.pop()

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


if __name__ == "__main__":
    string = '123456789'
    stack = MyStack()

    for i in string:
        stack.push(i)

    for i in stack:
        print(i, end=' ')
