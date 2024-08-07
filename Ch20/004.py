products = ['phone', 'tablets', 'laptops']
quantities = (343, 13, 74)

product_qtys = zip(products, quantities)
product_qtys_dict = dict(product_qtys)

for prod in product_qtys_dict:
    print(product_qtys_dict[prod])
