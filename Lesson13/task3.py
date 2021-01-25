# Напишите функцию под названием `choose_func`, которая принимает список из числа и 2
# функции обратного вызова. Если все числа внутри списка положительны, выполнить
# первую функцию в этом списке и вернуть ее результат. В противном случае вернуть результат второго


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(f1, f2):
    def result_choice(nums):
        for i in nums:
            if i < 0:
                return f2(nums)
        return f1(nums)
    return result_choice


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

test = choose_func(square_nums, remove_negatives)

print(test(nums1))
print(test(nums2))

