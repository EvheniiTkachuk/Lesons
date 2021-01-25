# Fraction
# Create a Fraction class, which will represent all basic arithmetic logic
# for fractions (+, -, /, *) with appropriate checking and error handling


class Fraction:
    def __init__(self, s):
        try:
            check = Fraction.check_input(s)
            self.a = check[0]
            self.b = check[1]
            self.string = s
        except (ValueError, TypeError):
            print('Error: Input string mast be type like: "1/2"')

    @staticmethod
    def check_input(s):
        try:
            flag = False
            num1 = ''
            num2 = ''
            while s:
                if s[0] == '/':
                    s = s[1:]
                    flag = True
                    continue
                if not flag:
                    num1 += s[0]
                else:
                    num2 += s[0]
                s = s[1:]
            num1, num2 = int(num1), int(num2)
            return [num1, num2]
        except:
            print('Error')

    def __add__(self, other):
        try:
            if self.b == other.b:
                return Fraction(str(str(self.a + other.a) + '/' + str(self.b)))
        except (AttributeError, TypeError):
            return 'Error'

    def __repr__(self):
        try:
            return self.string
        except (AttributeError, TypeError):
            return 'AttributeError or TypeError in __repr__'

    def __str__(self):
        try:
            return self.string
        except (AttributeError, TypeError):
            return 'AttributeError or TypeError in __str__'


x = Fraction('2/5')
y = Fraction('1/5')
print(x)
print(y)
res = x + y
print(res)


s = 8000 * 0.0001 / 30 * 15
print(s)