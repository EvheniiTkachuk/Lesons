def power(a, b):
    try:
        a = int(a)
        b = int(b)
    except (TypeError, ValueError):
        print('The entered value must be integer or float')
    else:
        try:
            return (a / b) * (a / b)
        except ZeroDivisionError:
            print('Divide by zero')
            return 0


while True:
    res = power(a=input('Enter \'a\': '), b=(input('Enter \'b\': ')))
    if not res:
        continue
    else:
        print(f'Result expression (a / b) * (a / b) = {res}')
        break

