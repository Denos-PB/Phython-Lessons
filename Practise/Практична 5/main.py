from data_input import input_product
from calculation import calculate_stock_value, calculate_discount
from general import print_product_name, find_product

products = input_product()
print(products)

calculate_stock_value(products)

calculate_discount(products)

product_names = list(products.keys())
print_product_name(product_names)

find_product(products, print("Enter product name to search: "))