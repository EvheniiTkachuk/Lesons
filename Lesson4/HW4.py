from random import randint as rand

# task1 [The Guessing Game]

while True:
    numPlayer = input('Enter your number: ')
    if not numPlayer.isdigit():
        print('Please, enter correct number in range (1 - 10)')
        continue
    numPlayer = int(numPlayer)
    if numPlayer <= 0 or numPlayer >= 11:
        print('Please, enter correct number in range (1 - 10)')
        continue
    else:
        numGenerate = rand(1, 10)
        if numGenerate == numPlayer:
            print(f'{numGenerate} is Computer number! YOU WIIIIIIN!')
            break
        else:
            print(f'{numGenerate} is Computer number! TRY AGAIN!')



# task2 [The birthday greeting program]

while True:
    name = input('Enter your name: ')
    if not name.isalpha():
        print('Please, enter correct name: ')
        continue
    else:
        break
while True:
    age = input('Enter your age: ')
    if not age.isdigit():
        print('Please, enter correct age: ')
        continue
    else:
        age = int(age)
        if age <= 0 or age >= 121:
            print('Please, enter correct age: ')
            continue
        break

print(f'Hello, {str.title(name)}, on your next birthday you’ll be {age + 1} years')



# task3 [Words combination]

while True:
    strEnter = input('Enter string: ')
    if not strEnter.isalpha():
        print('Please, enter correct string: ')
        continue
    else:
        break
index = None
i = 0
strIntermediate = ''
strResult = ''
while i < 5:
    j = len(strEnter)
    strResult = ''
    strIntermediate = strEnter
    while j != 0:
        index = rand(0, len(strIntermediate) - 1)
        strResult += strIntermediate[index]
        strIntermediate = strIntermediate[:index] + strIntermediate[index + 1: len(strIntermediate)]
        j -= 1
    print(f'Str[{i+1}] = \'{strResult}\'')
    i += 1



# task4 [The math quiz program]

from pandas import eval

while True:
    while True:
        countNum = input('Enter count number: ')
        if not countNum.isdigit():
            print('Please, enter correct number in range (2 - 10)')
            continue
        countNum = int(countNum)
        if countNum <= 1 or countNum >= 11:
            print('Please, enter correct number in range (2 - 10)')
            continue
        else:
            break

    i = 0
    expression = ''
    operations = '+-*/'
    while i < countNum:
        if i == countNum - 1:
            expression += str(rand(1, 100))
        else:
            expression += str(rand(1, 100)) + ' ' + operations[rand(0, len(operations) - 1)] + ' '
        i += 1

    resEval = round(eval(expression), 2)
    result = type(resEval)(input(f'Enter result:\n{expression} = '))
    result = (round(result, 2))
    if result == resEval:
        choice = input('You\'re right! this answer is correct!\nOne more time? (Y/N): ')
    else:
        choice = input('You made a mistake!\nOne more time? (Y/N): ')
    if str.lower(choice) == 'y':
        continue
    else:
        print(f'Thank you for use!')
        break

