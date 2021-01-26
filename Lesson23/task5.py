#############################################
# All tasks should be solved using recursion
#############################################


def sum_of_digits(digit_string: str) -> int:
    if not digit_string.isdigit():
        raise ValueError("input string must be digit string")
    elif len(digit_string) <= 1:
        return int(digit_string)
    else:
        return int(digit_string) % 10 + int(sum_of_digits(digit_string[:-1]))


print(sum_of_digits('11111'))  # == 5
print(sum_of_digits('26'))  # == 8
print(sum_of_digits('test'))  # == ValueError("input string must be digit string")
