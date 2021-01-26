#############################################
# All tasks should be solved using recursion
#############################################


def is_palindrome(looking_str: str) -> bool:
    if len(looking_str) <= 2:
        return True
    elif looking_str[0] != looking_str[-1]:
        return False
    else:
        return is_palindrome(looking_str[1:-1])


print(is_palindrome('mom'))  # True
print(is_palindrome('sassas'))  # True
print(is_palindrome('o'))  # True
print(is_palindrome('absdefg'))  # Flase