products = ['phone', 'tablets', 'laptops']
quantities = (343, 13, 74)
tags = 'abs'

prod_qtys = zip(products, quantities, tags)

print(prod_qtys)
print(type(prod_qtys))

for product in prod_qtys:
    print(product)
    print(product[0])


