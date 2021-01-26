#############################################
# All tasks should be solved using recursion
#############################################


def mult(a: int, n: int) -> int:
    if n == 0:
        return 0
    elif n < 0:
        raise ValueError("This function works only with postive integers")
    else:
        return a + mult(a, n - 1)


print(mult(2, 4))  # == 8
print(mult(2, 0))  # == 0
print(mult(2, -4))  # == Error

