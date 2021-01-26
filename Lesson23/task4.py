#############################################
# All tasks should be solved using recursion
#############################################


def reverse(input_str: str) -> str:
    if len(input_str) <= 1:
        return input_str
    else:
        return input_str[-1] + reverse(input_str[:len(input_str) - 1])


print(reverse('12345'))  # 54321
print(reverse("hello"))  # == "olleh"
