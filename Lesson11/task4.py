import traceback
import sys


class CustomException(Exception):
    count_error = 0

    def __init__(self, text_error):
        self.text_error = text_error
        self.line = 0

    def write_to_file(self, file_name='log.txt'):
        CustomException.get_line_error(self)
        with open(file_name, 'a') as write_file:
            CustomException.count_error += 1
            write_file.write(f'{CustomException.count_error}. {self.text_error}  | in line {self.line}\n')

    def get_line_error(self):
        for frame in traceback.extract_tb(sys.exc_info()[2]):
            frame, lineno, fn, text = frame
            self.line = lineno

    @staticmethod
    def reset__data_file(file_name='log.txt'):
        with open(file_name, 'w') as write_file:
            pass


CustomException.reset__data_file()
try:
    raise CustomException('//////////test except//////////')
except CustomException as cs:
    cs.write_to_file()



class Product:
    def __init__(self, type_prod, name, price):
        self.type_prod = type_prod
        self.name = name
        self.price = price

    def __repr__(self):
        return f'type: {self.type_prod} | name: {self.name} | price: {self.price}'

    def __str__(self):
        return f'type: {self.type_prod} | name: {self.name} | price: {self.price}'


class ProductStore():
    total_sales = 0

    def __init__(self):
        self.prod_list = []

    def add(self, product, amount):
        try:
            if not (isinstance(product, Product)) or not (type(amount) is int):
                raise CustomException('Product must be type Product, amount must be type int')
            product.price += round((product.price * 0.3), 2)
            self.prod_list.append([product, amount])
        except CustomException as cs:
            print('ValueError: product must be type Product, amount must be type int')
            cs.write_to_file()

    def set_discount(self, identifier, percent, identifier_type='name'):
        try:
            if not (type(percent) is int) or (not (identifier_type == 'name' or identifier_type == 'type')):
                raise CustomException('Percent must be int, identifier_type must be "name" or "type"')
            for i in self.prod_list:
                if identifier_type == 'name' and i[0].name == identifier:
                    i[0].price -= round((i[0].price * (percent / 100)), 2)
                    break
                elif identifier_type == 'type' and i[0].type_prod == identifier:
                    i[0].price -= round((i[0].price * (percent / 100)), 2)
                    break
            else:
                print('Product not found')
        except CustomException as cs:
            print('ValueError: Percent must be int, identifier_type must be "name" or "type"')
            cs.write_to_file()

    def sell_product(self, product_name, amount=1):
        try:
            if not (type(amount) is int):
                raise CustomException('Amount must be type int')
            for i in self.prod_list:
                if i[0].name == product_name:
                    try:
                        if amount <= i[1]:
                            i[1] -= amount
                            ProductStore.total_sales += i[0].price * amount
                            break
                        else:
                            raise CustomException('Don\'t enough product')
                    except CustomException as cs:
                        print('ValueError: not enough product')
                        cs.write_to_file()
                        return
            else:
                print('Product not found')
        except CustomException as cs:
            print('ValueError: amount must be type int')
            cs.write_to_file()
            return

    def get_product_info(self, product_name):
        for i in self.prod_list:
            if i[0].name == product_name:
                return [(val[0], val[1]) for val in self.prod_list if val[0].name == product_name][0]
        else:
            return 'Product not found'

    @staticmethod
    def get_income():
        return f'\nTotal income: {ProductStore.total_sales}'

    def get_all_product(self):
        return '\nProduct in store:\n' + '\n'.join(f'{i + 1}. ({j[0]}), amount = {j[1]}' for i, j in enumerate(self.prod_list))

    def __repr__(self):
        return '\nProduct in store:\n' + '\n'.join(f'{i + 1}. ({j[0]}), amount = {j[1]}' for i, j in enumerate(self.prod_list))


prod1 = Product('Technique', 'TV', 1000)
prod2 = Product('Fruit', 'apple', 10)
prod3 = Product('Decor', 'Picture', 10000)

store = ProductStore()
store.add(prod1, 10)
store.add(prod2, 10)
store.add(prod3, 10)
# ValueError
store.add('abc', 10)
store.add(prod3, '10')

print(store.get_all_product())
store.set_discount('TV', 15)
store.set_discount('Fruit', 10, 'type')
# ValueError
store.set_discount('TV1', '10')
store.set_discount('Fruit1', 10, 'name_type')
# ValueError product not found
store.set_discount('Beer', 10,)

print(store.get_all_product())

store.sell_product('TV')
store.sell_product('Picture', 5)

# ValueError amount must be type int
store.sell_product('Picture', '5')
# ValueError not enough product
store.sell_product('Picture', 20)
# ValueError product not found
store.sell_product('Beer', 5)


print(store.get_all_product())
print(store.get_income())  # == print(store)

print(store.get_product_info('TV'))
# product not found
print(store.get_product_info('Beer'))