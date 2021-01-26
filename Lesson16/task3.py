class Iterator:

    def __iter__(self):
        return self

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.counter
        else:
            raise StopIteration

    def __getitem__(self, item):
        return item


itr = Iterator(5)

for i in itr:
    print(i, end=' ')

print(f'\nget item index 5: {itr[5]}')

