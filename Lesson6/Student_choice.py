from random import choice

my_dict = {
    1: 'Женя Ткачук',
    2: 'Anna Mikhalchuk',
    3: 'Женя Дубенко',
    4: 'Yuriy',
    5: 'Артём Селиванов',
    6:' Mimimishka',
    7:' Dmitriy Shelekhov',
    8:' Кateryna',
    9:' Oksana',
    10: 'Dan',
    11: 'Евгений Свиридов',
    12: 'Oleg Kashyrin'
}

while my_dict:
    print(my_dict.pop(choice(tuple(my_dict.keys()))))
    s = input('One more time? (Y/any key): ')
    if s.lower() == 'y':
        continue
    else:
        print('Thanks for using! ◕‿◕')
        break
else:
    print('No students left  ¯\_ツ_/¯  ')