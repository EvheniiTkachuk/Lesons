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


class Queue:
    def __init__(self):
        self._head = None
        self._next = None
        self._tail = None

    def is_empty(self):
        return bool(self._head)

    def enqueue(self, item):
        new_node = Node(item)
        if self._head is None:
            self._head = new_node
            self._tail = self._head
        else:
            self._tail.set_next(new_node)
            self._tail = new_node

    def dequeue(self):
        if Queue.is_empty(self):
            temp = self._head
            self._head = self._head.get_next()
            return temp

    def peek(self):
        return self._head

    def __repr__(self):
        name = 'Queue'
        string = ''
        current = self._head
        while current:
            string += ' ' + str(current.get_data())
            current = current.get_next()
        return f'{name}:{string}'

    def __str__(self):
        return Queue.__repr__(self)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    print(queue)

    print()
    print(f'queue.pop(): {queue.dequeue()}')
    print(queue)

    print()
    print(f'queue.peek(): {queue.peek()}')
    print(queue)
