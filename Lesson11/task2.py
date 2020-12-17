class Mathematician:

    @staticmethod
    def square_nums(numbers_list):
        return [num * num for num in numbers_list]

    @staticmethod
    def remove_positives(numbers_list):
        return [num for num in numbers_list if num < 0]

    @staticmethod
    def filter_leaps(numbers_list):
        return [num for num in numbers_list if num % 4 == 0]


m = Mathematician()

num_list = [1, 2, 3, 4, 5]
print(f'Default list: {num_list}')
print(f'Square_nums: {m.square_nums(num_list)}')

num_list = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]
print(f'\nDefault list: {num_list}')
print(f'Remove_positives: {m.remove_positives(num_list)}')

num_list = [2001, 1884, 1995, 2003, 2020]
print(f'\nDefault list: {num_list}')
print(f'Filter_leaps: {m.filter_leaps(num_list)}')
