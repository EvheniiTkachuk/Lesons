# Extracting numbers.
# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

list1 = list(range(1, 101))
listRes = []
i = 0
while i < len(list1):
    if list1[i] % 7 == 0 and list1[i] % 5 != 0:
        listRes.append(list1[i])
    i += 1
print(f'Result list that are divisible by 7 but not a multiple of 5:  {listRes}')

