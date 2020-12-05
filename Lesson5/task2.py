# Exclusive common numbers.
# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common
# integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

from random import randint as rand

i = 0
list1 = []
list2 = []
listRes = []
while i < 10:
    list1.append(rand(1, 10))
    list2.append(rand(1, 10))
    i += 1

i = 0
while i < 10:
    if list1[i] in list2 and not list1[i] in listRes:
        listRes.append(list1[i])
    i += 1

print(list1, list2, sep='\n')
print('Result = ', listRes)
