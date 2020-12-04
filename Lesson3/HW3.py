# task1 [String manipulation]

strings = ['Hello, World', 'my', 'x', '1100000022', 'PYT', '']
i = 0
while i < len(strings):
    strLen = len(strings[i])
    if strLen > 2:
        print(f'{strings[i]} -', strings[i][:2] + strings[i][-2: strLen])
    elif strLen < 2:
        print(f'{strings[i]} -', 'Empty String')
    else:
        print(f'{strings[i]} -', strings[i] * 2)
    i += 1



# task2 [The valid phone number program]

numbers = ['5268475123', 'Not number', '12345', '3214759683', '1111FFF1111']
i = 0
while i < len(numbers):
    if numbers[i].isdigit() and len(numbers[i]) == 10:
        print(f'{numbers[i]} - VALID')
    else:
        print(f'{numbers[i]} - ERROR')
    i += 1




# task3 [The name check]

name = 'evhenii'
while True:
    print('\nEnter your name: ')
    inputName = input()
    if name == inputName.lower():
        print('\nName - OK')
        break
    else:
        print('You wrong!')
