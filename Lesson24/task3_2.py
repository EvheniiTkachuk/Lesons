# Extend the Queue to include a method called get_from_stack that
# searches and returns an element e from a queue. Any other element must
# remain in the queue respecting their order. Consider the case in which the element
# is not found - raise ValueError with proper info Message


class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def get_from_queue(self, item):
        try:
            return self._items.pop(self._items.index(item))
        except (ValueError, TypeError):
            print(f'\nItem "{item}" don\'t found')

    def __iter__(self):
        self.index = len(self._items) - 1
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        self.index -= 1
        return self._items[self.index + 1]

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items), 1):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    string = '123456789'
    queue = Queue()

    for i in string:
        queue.enqueue(i)

    for i in queue:  # __iter__, __next__
        print(i, end=' ')
    print()

    print(queue)

    queue.get_from_queue('9')
    queue.get_from_queue('8')
    queue.get_from_queue('7')
    print(queue)

    queue.get_from_queue('5')
    queue.get_from_queue('4')
    queue.get_from_queue('3')
    queue.get_from_queue('2')
    print(queue)

    queue.get_from_queue('test')
