# Make a program that has some sentence (a string) on input and returns a dict containing
# all unique words as keys and the number of occurrences as values.

test_str = 'Мені тринадцятий минало. Я пас ягнята за селом. Чи то так сонечко сіяло, Чи так мені чого було? '\
           'Мені так любо, любо стало, Неначе в Бога... Уже прокликали до паю, А я собі у бур’яні ' \
           'Молюся Богу... І не знаю, Чого маленькому мені Тойді так приязно молилось, Чого так весело було.'

# test_str = 'a ff, ff. ggg... ggg? ggg!     tttt tttt     tttt tttt, "ppppp" ppppp ppppp. ppppp/ppppp'

chars = '.,!?:;\"\'\\/'
clear_str = test_str.lower()

for c in chars:
    clear_str = clear_str.replace(c, ' ')

print('Строка без символов:  ' + clear_str)
words_list = clear_str.split()
print(f'Список слов:  {words_list}')

dict_res = dict.fromkeys(words_list, 0)
print(f'Исходный словарь:  {dict_res}')

print('\n\nКоличество слов:')
for key in dict_res.keys():
    dict_res[key] = words_list.count(key)
    print(f'{key} - {dict_res[key]}')

