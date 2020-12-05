# Create a function which takes as input two dicts with structure mentioned above,
# then computes and returns the total price of stock.

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total_price = 0
for key, val in stock.items():
    temp_price = round(float(val * prices[key]), 2)
    print(key, ' - ', val, 'x', prices[key], '=', format(temp_price, '.2f'))
    total_price += temp_price
print('Total price = ', format(total_price, '.2f'))
