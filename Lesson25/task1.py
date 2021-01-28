# Implement append, index, pop, insert methods for UnorderedList.
# Also implement a slice method, which will take two parameters `start` and `stop`,
# and return a copy of the list starting at the position and going
# up to but not including the stop position.


class Node:

    def __init__(self, data):
        self._data = data
        self._next = None
        self._index = 0

    def get_data(self):
        return self._data

    def get_index(self):
        return self._index

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, new_next):
        self._next = new_next


class UnorderedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self.count = 0

    def is_empty(self):
        return self._head is None

    def add(self, item):
        new_node = Node(item)
        temp = self._head
        self._head = new_node
        new_node.set_next(temp)
        new_node._index = 0
        current = temp
        i = 0
        while not (current is None):
            current._index = i + 1
            i += 1
            current = current.get_next()

    def append(self, item):
        temp = Node(item)
        if self.count == 0:
            self._head = temp
            self._head._index = self.count
            self._tail = self._head
        else:
            self._tail.set_next(temp)
            self._tail = temp
            self._tail._index = self.count
        self.count += 1

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def index(self, item):
        current = self._head
        while current is not None:
            if current.get_data() == item:
                return current.get_index()
            else:
                current = current.get_next()

    def item(self, index):
        min_index = self._head.get_index()
        max_index = self._tail.get_index()
        if min_index <= index <= max_index:
            current = self._head
            while True:
                if current.get_index() == index:
                    return current
                current = current.get_next()

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def pop(self):
        current = self._head
        prev = current
        while True:
            if current.get_next() is None:
                prev.set_next(None)
                self._tail = prev
                return current
            else:
                prev = current
                current = current.get_next()

    def insert(self, index, item):
        min_index = self._head.get_index()
        max_index = self._tail.get_index()
        if index == 0:
            current = self._head
            self._head = Node(item)
            self._head.set_next(current)

            while not (current is None):
                current._index = index + 1
                index += 1
                current = current.get_next()
        elif index == self._tail.get_index():
            current = UnorderedList.item(self, index - 1)
            temp = current.get_next()
            temp._index = index + 1
            new_node = Node(item)
            new_node._index = index
            current.set_next(new_node)
            new_node.set_next(temp)

        elif not (min_index < index < max_index):
            raise ValueError(f'Index mast be in rang [{min_index} : {max_index}]')

        else:
            new_node = Node(item)
            current = UnorderedList.item(self, index - 1)
            new_node._index = index
            self.count += 1
            temp = current.get_next()
            current.set_next(new_node)
            new_node.set_next(temp)
            current = current.get_next()

            while not (current is None):
                current._index = index
                index += 1
                current = current.get_next()

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()}[{current.get_index()}] "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    my_list = UnorderedList()

    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)
    my_list.append(6)
    my_list.append(10)

    print(my_list.size())
    print(my_list)
    print(my_list.index(10))
    my_list.pop()
    print(my_list)

    my_list.insert(2, 111)
    print(my_list)

    my_list.insert(0, 111)
    print(my_list)

    my_list.insert(7, 111)
    print(my_list)

    my_list.add(222)
    print(my_list)
