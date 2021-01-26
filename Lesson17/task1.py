import unittest


def make_operation(operation, *args):
    res = 0
    if operation is '-':
        for j, i in enumerate(args):
            if j is 0:
                res = i
            else:
                res -= i
    elif operation is '+':
        for i in args:
            res += i
    elif operation is '*':
        res = 1
        for i in args:
            res *= i
    print(f'Result expression [', end='')
    for j, i in enumerate(args):
        if i < 0 and j < len(args) - 1:
            print(f'({i}) {operation} ', end='')
        elif i < 0:
            print(f'({i})', end='')
        elif j < len(args) - 1:
            print(f'{i} {operation} ', end='')
        else:
            print(f'{i}', end='')
    print(f'] = {res}')
    return res


make_operation('+', 7, 7, 2)
make_operation('-', 5, 5, -10, -20)
make_operation('*', 7, 6)


class TestOperations(unittest.TestCase):

    def test_plus(self):
        operation = '+'
        args = (1, 1, 1, 1, 1)
        result = make_operation(operation, *args)
        self.assertEqual(result, 5)

    def test_plus1(self):
        operation = '+'
        args = (-1, -1, -1, -1, -1)
        result = make_operation(operation, *args)
        self.assertEqual(result, -5)

    def test_minus(self):
        operation = '-'
        args = (5, 1, 1, 1, 1)
        result = make_operation(operation, *args)
        self.assertEqual(result, 1)

    def test_minus1(self):
        operation = '-'
        args = (-10, -10, -10, -10, -10)
        result = make_operation(operation, *args)
        self.assertEqual(result, 30)

    def test_multy(self):
        operation = '*'
        args = (2, 2, 2, 2, 2)
        result = make_operation(operation, *args)
        self.assertEqual(result, 32)

    def test_multy1(self):
        operation = '*'
        args = (1, 1, 1, 1, 1)
        result = make_operation(operation, *args)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()