products = ['phone', 'tablets', 'laptops']
quantities = (343, 13, 74, 100)  # will ignore longer elements in sequences
tags = 'ab'  # will take only 2 elements as a zip TAPL because this is the shortest element

prod_qtys = zip(products, quantities, tags)

print(prod_qtys)
print(type(prod_qtys))

for product in prod_qtys:
    print(product)
    print(product[0])
