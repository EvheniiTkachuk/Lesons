class Node:
    def __init__(self, item):
        self._data = item
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_next(self, new_next):
        self._next = new_next

    def set_data(self, data):
        self._data = data

    def __repr__(self):
        return self._data

    def __str__(self):
        return str(self._data)


class MyStack:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return bool(self._head)

    def push(self, item):
        new_node = Node(item)
        if self._head is None:
            self._head = new_node
        else:
            new_node.set_next(self._head)
            self._head = new_node

    def pop(self):
        if MyStack.is_empty(self):
            temp = self._head
            self._head = self._head.get_next()
            return temp

    def peek(self):
        return self._head

    def __iter__(self):
        self.index = self._head
        return self

    def __next__(self):
        if self.index is None:
            raise StopIteration()
        result = self.index.get_data()
        self.index = self.index.get_next()
        return result

    def __repr__(self):
        name = 'Stack'
        string = ''
        current = self._head
        while current:
            string += ' ' + str(current.get_data())
            current = current.get_next()
        return f'{name}:{string}'

    def __str__(self):
        return MyStack.__repr__(self)


if __name__ == '__main__':
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack)

    print()
    print(f'stack.pop(): {stack.pop()}')
    print(stack)

    print()
    print(f'stack.peek(): {stack.peek()}')
    print(stack)


