#task 1

name = 'Carl'
day = 'Monday'
print('Good day, ' + name + '! ' + day + ' is a perfect day to learn some python.')
print('Good day, {name}! {day} is a perfect day to learn some python.'.format(name = name, day = day))
print(f'Good day, {name}! {day} is a perfect day to learn some python.')
print(f'Good day, %s! %s is a perfect day to learn some python.' % (name, day))


#task 2
name = 'Evhenii'
secondName = 'Tkachuk'

res = ' '.join([name, secondName])
print(f'Hello, {res}!')

print('Hello,', name, secondName + '!')
print('Hello, ' + name + ' ' + secondName + '!')


#task 3
a = 7
b = 4

print('a + b =', str(a + b))
print('a - b =', str(a - b))
print('a / b =', str(a / b))
print('a * b =', str(a * b))
print('a ** b =', str(a ** b))
print('a % b =', str(a % b))
print('a // b =', str(a // b))