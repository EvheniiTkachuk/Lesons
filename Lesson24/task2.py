# Write a program that reads in a sequence of characters,
# and determines whether it's parentheses, braces, and curly brackets are "balanced."


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


def check(string: str, stack: MyStack) -> bool:
    for i in string:
        if i == '(' or i == '{' or i == '[':
            stack.push(i)
        elif i == ')' and stack.peek() == '(':
            stack.pop()
        elif i == ']' and stack.peek() == '[':
            stack.pop()
        elif i == '}' and stack.peek() == '{':
            stack.pop()
    return True if stack.count() == 0 else False


if __name__ == "__main__":
    my_string = '{[()]}'
    my_string1 = '((((((('
    my_string2 = '{{{[]}}}'
    my_stack = MyStack()
    my_stack1 = MyStack()
    my_stack2 = MyStack()

    print(f'{my_string} = {check(my_string, my_stack)}')
    print(f'{my_string1} = {check(my_string1, my_stack1)}')
    print(f'{my_string2} = {check(my_string2, my_stack2)}')
